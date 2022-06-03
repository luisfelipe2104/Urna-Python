#--------------------------------------------------------------
# Banco de Candidatos

Candidatos = {"Godofredo": ["13", 0],
              "Rogério": ["17", 0],
              "Jurandi": ["56", 0],
              "Branco": ["Branco", 0]}

#--------------------------------------------------------------
# Eleição

def Eleição(Candidatos):
# variáveis

    Nulo = 0
    VotosTotais = 0
    SenhaUrna = "123"
    UrnaOn = True

#-----------------------------------------------------------
# Senha e Confirmação da senha

    while UrnaOn:
        
        senha = None
        confirmarSenha = None
        print()
        print("------------------------------------")
        while not senha:
            senha = input("Digite sua senha: ")

            
        while confirmarSenha != senha:
            confirmarSenha = input("Confirme sua senha: ")

#-----------------------------------------------------------
# Candidatos

        print()
        print("------------------------------------")
        print("---Vote consciente----")
        print("------Candidatos------")
        for key, value in Candidatos.items():
            if key != "Branco":
                print(f"------{key}: {value[0]}-----")
        print("                         |Branco|")
        print("------------------------------------")
        
#-----------------------------------------------------------
# input do usuário

        print()
        voto = input("Para quem será seu voto? ")

#-----------------------------------------------------------
# Validando os votos

        NumCandidato = []
        for key, value in Candidatos.items():
            NumCandidato.append(value[0])

        
        for i in NumCandidato:
            if i == voto:
                for key, value in Candidatos.items():
                    if value[0] == voto:
                        VotosTotais +=1
                        value[1] +=1
        
#-----------------------------------------------------------
# Caso o voto seja nulo

        if voto not in NumCandidato:
            Nulo +=1
            VotosTotais +=1

#-----------------------------------------------------------
# Encerra ou continua a votação

        print()
        print("------------------------------------")
        encerrarVotação = ""
        while encerrarVotação not in ['1', '2']:
            encerrarVotação = input("Digite 1 para ENCERRAR a votação \nDigite 2 para CONTINUAR a votação\n").upper()

        print("------------------------------------")
        ValidarSenha = ""
        while ValidarSenha != SenhaUrna:
            ValidarSenha = input("Digite a senha da urna: ")


#-----------------------------------------------------------
# Votação encerrada

        if encerrarVotação == "1":
            UrnaOn = False
            print()
            print("-----------------------------------------------------------------------")
            print("---------------Votação encerrada---------------")
            print()

#-----------------------------------------------------------
# Contabilizando os votos 

    VotosCandidatos = []
    for key, value in Candidatos.items():
        VotosCandidatos.append(value[1])

    VotosInválidos = Nulo + Candidatos["Branco"][1]
            
    VotosVálidos = VotosTotais - (VotosInválidos)

#------------------------------------------------------------------------------------------
# Candidato(s) vencedor(es)

    CandidatoVencedor = max(VotosCandidatos[0], VotosCandidatos[1], VotosCandidatos[2])

#--------------------------------------------------------------------------------------------
# Definindo o candidato eleito

    SegundoTurno = {}

    for key, value in Candidatos.items():
        if value[1] == CandidatoVencedor and CandidatoVencedor > 0:
            SegundoTurno.update({key: [value[0], value[1]]})
            if CandidatoVencedor > 0:
                Eleito = key

# --------------------------------------------------------------------------
# Caso tenha segundo turno

    if len(SegundoTurno) > 1:
        NomeCandidatoSegundoTurno = []
        for i in SegundoTurno.keys():
            NomeCandidatoSegundoTurno.append(i)

        try:
            print(f"Teremos um segundo turno entre {NomeCandidatoSegundoTurno[0]} e {NomeCandidatoSegundoTurno[1]} e {NomeCandidatoSegundoTurno[2]}")
        except:
            print(f"Teremos um segundo turno entre {NomeCandidatoSegundoTurno[0]} e {NomeCandidatoSegundoTurno[1]}")

# --------------------------------------------------------------------------
# Resetando os votos e iniciando o segundo turno

        for key, value in SegundoTurno.items():
            value[1] = 0

        SegundoTurno.update({"Branco": ["Branco", 0]})

        Eleição(SegundoTurno)
#-----------------------------------------------------------------------------
# Convertendo para porcentagem e fazendo o output

    else:
        for key, value in Candidatos.items():
            try:
                valuePercent = (value[1]/VotosVálidos) * 100
            except ZeroDivisionError:
                valuePercent = 0

            if key != "Branco":
                print(f"---------{key}: {round(valuePercent)}% --- Valor aboluto: {value[1]} voto(s)----------")
        
#------------------------------------------------------------------------------
# final
        try:
            percentVálidos = round((VotosVálidos/VotosTotais) * 100)
        except ZeroDivisionError:
            percentVálidos = 0

        try:
            percentInválidos = round((VotosInválidos/VotosTotais) * 100)
        except ZeroDivisionError:
            percentInválidos = 0

        brancos = Candidatos["Branco"][1]
        print()
        print("------------------------------------")
        print(f"Votos totais: {VotosTotais}\nVotos válidos: {percentVálidos}% ({VotosVálidos} votos)")
        print(f"Votos inválidos: {percentInválidos}% (Brancos: {brancos}, Nulos: {Nulo})")
        print()
        print("------------------------------------")
        try:
            print(f"-------Candidato eleito: {Eleito}-------")
            
        # caso ninguém tenha recebido voto
        except:
            print(f"-------Candidato eleito: Nenhum-------")

        print("------------------------------------")

Eleição(Candidatos)