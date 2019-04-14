import web
import config as config

db = config.db


def get_all_asesorias():
    try:
        return db.select('asesorias')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asesorias(num_as):
    try:
        return db.select('asesorias', where='num_as=$num_as', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def get_asesor(asesor):
        try:
            return db.select('asesorias', where="asesor = $asesor", vars=locals())
        except Exception as e:
            print "Model get Error {}".format(e.args)
            print "Model get Message {}".format(e.message)
            return None

def get_asesor_estado(asesor,estado):
        try:
            return db.select('asesorias', where='asesor = $asesor'and 'estado = $estado',vars=locals() )
        except Exception as e:
            print "Model get Error {}".format(e.args)
            print "Model get Message {}".format(e.message)
            return None

def get_solicitante_estado(asesor,estado):
        try:
            return db.select('asesorias', where='asesor = $asesor'and 'estado = $estado',vars=locals() )
        except Exception as e:
            print "Model get Error {}".format(e.args)
            print "Model get Message {}".format(e.message)
            return None

def get_solicitante(solicitante):
        try:
            return db.select('asesorias', where="solicitante = $solicitante", vars=locals())
        except Exception as e:
            print "Model get Error {}".format(e.args)
            print "Model get Message {}".format(e.message)
            return None


def delete_asesorias(num_as):
    try:
        return db.delete('asesorias', where='num_as=$num_as', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_asesorias(dia,hora,estado,solicitante,asesor,tema):
    try:
        return db.insert('asesorias',dia=dia,
hora=hora,
estado=estado,
solicitante=solicitante,
asesor=asesor,
tema=tema)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_asesorias(num_as,dia,hora,estado,solicitante,asesor,tema):
    try:
        return db.update('asesorias',num_as=num_as,
dia=dia,
hora=hora,
estado=estado,
solicitante=solicitante,
asesor=asesor,
tema=tema,
                  where='num_as=$num_as',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
