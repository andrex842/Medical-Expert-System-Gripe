from experta import *


diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n") 
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease symptoms/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Disease descriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Disease treatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("La enfermedad más probable que tengas es %s\n" %(id_disease))
		print("A continuación se ofrece una breve descripción de la enfermedad:\n")
		print(disease_details+"\n")
		print("Los medicamentos y procedimientos comunes sugeridos por otros médicos reales son: \n")
		print(treatments+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Vomito, Dolor_de_garganta, Flema,Dificultad_para_respirar ,Diarrea,Malestar_en_la_garganta,Dolor_en_los_huesos,Rx_del_pulmon_con_mancha):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("¡Hola! Soy el Dr.Yar, estoy aquí para ayudarte a mejorar tu salud.")
		print("Para eso tendrás que responder algunas preguntas sobre tus condiciones.")
		print("¿Sientes alguno de los siguientes síntomas?:")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(Fiebre=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(Fiebre=input("Fiebre mayor a 38.5: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Tos=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(Tos=input("Tos: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Moco=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(Moco=input("Moco: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Congestion_nasal=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(Congestion_nasal=input("Congestion nasal: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Estornudos=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(Estornudos=input("Estornudos: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Dolor_de_garganta=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(Dolor_de_garganta=input("Dolor de garganta: ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(Malestar_en_la_garganta=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(Malestar_en_la_garganta=input("Malestar en la garganta: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Dificultad_para_respirar=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(Dificultad_para_respirar=input("Dificultad para respirar: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Flema=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(Flema=input("Flema: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Vomito=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(Vomito=input("Vomito: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(Diarrea=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(Diarrea=input("Diarrea: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(Debilidad_Cansancio=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(Debilidad_Cansancio=input("Debilidad y/o Cansancio: ")))
                
	@Rule(Fact(action='find_disease'), NOT(Fact(Dolor_en_los_huesos=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(Dolor_en_los_huesos=input("Dolor en los huesos: ")))
    
	@Rule(Fact(action='find_disease'), NOT(Fact(Rx_del_pulmon_con_mancha=W())),salience = 1)
	def symptom_13(self):
		self.declare(Fact(Rx_del_pulmon_con_mancha=input("Rx del pulmón con mancha: ")))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="yes"),Fact(Tos="yes"),Fact(Moco="no"),Fact(Congestion_nasal="no"),Fact(Estornudos="no"),Fact(Dolor_de_garganta="yes"),Fact(Malestar_en_la_garganta="yes"),Fact(Dificultad_para_respirar="yes"),Fact(Flema="yes"),Fact(Vomito="yes"),Fact(Diarrea="yes"),Fact(Debilidad_Cansancio="yes"),Fact(Dolor_en_los_huesos="no"),Fact(Rx_del_pulmon_con_mancha="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Covid-19"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="yes"),Fact(Tos="yes"),Fact(Moco="yes"),Fact(Congestion_nasal="no"),Fact(Estornudos="yes"),Fact(Dolor_de_garganta="no"),Fact(Malestar_en_la_garganta="no"),Fact(Dificultad_para_respirar="no"),Fact(Flema="yes"),Fact(Vomito="yes"),Fact(Diarrea="yes"),Fact(Debilidad_Cansancio="no"),Fact(Dolor_en_los_huesos="yes"),Fact(Rx_del_pulmon_con_mancha="no"))
	def disease_1(self):
		self.declare(Fact(disease="Gripe"))

	@Rule(Fact(action='find_disease'),Fact(Fiebre="no"),Fact(Tos="yes"),Fact(Moco="no"),Fact(Congestion_nasal="yes"),Fact(Estornudos="yes"),Fact(Dolor_de_garganta="yes"),Fact(Malestar_en_la_garganta="yes"),Fact(Dificultad_para_respirar="no"),Fact(Flema="no"),Fact(Vomito="no"),Fact(Diarrea="no"),Fact(Debilidad_Cansancio="no"),Fact(Dolor_en_los_huesos="no"),Fact(Rx_del_pulmon_con_mancha="no"))
	def disease_2(self):
		self.declare(Fact(disease="Resfrio"))
        
	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("La enfermedad más probable que tengas es %s\n" %(id_disease))
		print("A continuación se ofrece una breve descripción de la enfermedad:\n")
		print(disease_details+"\n")
		print("Los medicamentos y procedimientos comunes sugeridos por otros médicos reales son: \n")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
       Fact(Fiebre=MATCH.Fiebre),
       Fact(Tos=MATCH.Tos),
       Fact(Moco=MATCH.Moco),
       Fact(Congestion_nasal=MATCH.Congestion_nasal),
       Fact(Estornudos=MATCH.Estornudos),
       Fact(Dolor_de_garganta=MATCH.Dolor_de_garganta),
       Fact(Malestar_en_la_garganta=MATCH.Malestar_en_la_garganta),
       Fact(Dificultad_para_respirar=MATCH.Dificultad_para_respirar),
       Fact(Flema=MATCH.Flema),
       Fact(Vomito=MATCH.Vomito),
       Fact(Diarrea=MATCH.Diarrea),
       Fact(Debilidad_Cansancio=MATCH.Debilidad_Cansancio),
       Fact(Dolor_en_los_huesos=MATCH.Dolor_en_los_huesos),
       Fact(Rx_del_pulmon_con_mancha=MATCH.Rx_del_pulmon_con_mancha),NOT(Fact(disease=MATCH.disease)),salience = -999)
    
	def not_matched(self,Fiebre,Tos,Moco,Congestion_nasal,Estornudos,Dolor_de_garganta,Malestar_en_la_garganta,Dificultad_para_respirar,Flema,Vomito,Diarrea,Debilidad_Cansancio,Dolor_en_los_huesos,Rx_del_pulmon_con_mancha):
		print("\nNo encontré ninguna enfermedad que coincida exactamente con sus síntomas.")
		lis = [Fiebre,Tos,Moco,Congestion_nasal,Estornudos,Dolor_de_garganta,Malestar_en_la_garganta,Dificultad_para_respirar,Flema,Vomito,Diarrea,Debilidad_Cansancio,Dolor_en_los_huesos,Rx_del_pulmon_con_mancha]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Algun otro sintoma que quiera registrar?")
		if input() == "no":
			exit()
		#print(engine.facts)