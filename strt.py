woods_cost = {
	'yasen': 3900
}
formuls = {}


def calculator(calc_func):
	formuls[calc_func.__name__] = calc_func
	return calc_func

@calculator
def func_window(quatity, heigth, wigth, wood, marsh, heigth_o=0, wigth_o=0):
	total = (heigth + wigth + heigth_o + wigth_o) * quatity * woods_cost[wood] * marsh / 500
	return total

@calculator
def func_door(quatity, heigth, wigth, wood, wall_thick, marsh):
	total = (((2 * heigth + wigth) * wall_thick) + (wall_thick * wigth) ) / 1000 * quatity * woods_cost[wood] * marsh
	return total

order = func_window(2, 2.3, 0.7, 'yasen', 3)
print(order)
