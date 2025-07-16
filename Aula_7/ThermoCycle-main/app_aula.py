from src.connector import Connector
from src.equipment.turbine import Turbine
from src.equipment.heater import Heater
from src.equipment.condenser import Condenser
from src.equipment.pump import Pump
from src.equipment.mixing_chamber import MixingChamber
from src.equipment.heat_exchanger import HeatExchanger
from src.thermoCycle import ThermoCycle

pipe_1 = Connector("pipe_1")
pipe_2 = Connector("pipe_2")
pipe_3 = Connector("pipe_3")
pipe_4 = Connector("pipe_4")
pipe_5 = Connector("pipe_5")
pipe_6 = Connector("pipe_6")
pipe_7 = Connector("pipe_7")
pipe_8 = Connector("pipe_8")
pipe_9 = Connector("pipe_9")

heater = Heater("heater")
turbine = Turbine("turbine")
condenser = Condenser("condenser")
pump_I = Pump("pump_I")
pump_II = Pump("pump_II")
mixing_chamber = MixingChamber("mixing_chamber")
heat_exchanger = HeatExchanger("heat_exchanger")

heater.add_connectors_in(pipe_5)
heater.add_connectors_out(pipe_6)

turbine.add_connectors_in(pipe_6)
turbine.add_connectors_out(pipe_7)
turbine.add_connectors_out(pipe_8)

condenser.add_connectors_in(pipe_8)
condenser.add_connectors_out(pipe_1)

pump_I.add_connectors_in(pipe_1)
pump_I.add_connectors_out(pipe_2)

pump_II.add_connectors_in(pipe_3)
pump_II.add_connectors_out(pipe_4)

heat_exchanger.add_connectors_in(pipe_2)
heat_exchanger.add_connectors_out(pipe_9)
heat_exchanger.add_connectors_in(pipe_7)
heat_exchanger.add_connectors_out(pipe_3)

mixing_chamber.add_connectors_in(pipe_9)
mixing_chamber.add_connectors_in(pipe_4)
mixing_chamber.add_connectors_out(pipe_5)

rankine_power_cycle = ThermoCycle()
rankine_power_cycle.add_equipment(pump_I)
rankine_power_cycle.add_equipment(turbine)
rankine_power_cycle.add_equipment(condenser)
rankine_power_cycle.add_equipment(heater)
rankine_power_cycle.add_equipment(heat_exchanger)
rankine_power_cycle.add_equipment(pump_II)
rankine_power_cycle.add_equipment(mixing_chamber)

rankine_power_cycle.initialize()
rankine_power_cycle.draw("app_aula_01.png")