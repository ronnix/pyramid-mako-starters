from pyramid.scaffolds import PyramidTemplate


class StarterMakoTemplate(PyramidTemplate):
    _template_dir = 'starter_mako'
    summary = 'Pyramid starter project (with Mako templates)'


class AlchemyMakoTemplate(PyramidTemplate):
    _template_dir = 'alchemy_mako'
    summary = 'Pyramid SQLAlchemy project using url dispatch (with Mako templates)'
