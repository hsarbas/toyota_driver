import pandas as pd
import csv
from collections import Counter
import itertools


def main():
    df = pd.read_csv("vehicle data.csv")

    # count number of vehicles per record, transform to dict, and output to csv
    crash_count = df.pivot_table(columns=['record_id'], aggfunc='size').to_dict()
    # with open('vehicle count.csv', 'w') as f:
    #     for key, value in crash_count.items():
    #         f.write("%s,%s\n" % (key, value))

    # ONE VEHICLE CRASHES
    vehicle_types = []
    for key, value in crash_count.items():
        if value == 1:
            with open('vehicle data.csv', newline='', encoding="utf-8-sig") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if key == row['record_id']:
                        vehicle_types.append(row['Vehicle type'])

    single_vehicle_dict = dict((x, vehicle_types.count(x)) for x in set(vehicle_types))
    with open('one vehicle.csv', 'w') as f:
        for key, value in single_vehicle_dict.items():
            f.write("%s,%s\n" % (key, value))

    # TWO VEHICLE CRASHES
    # two_vehicles_dict = dict()
    # for key, value in crash_count.items():
    #     if value == 2:
    #         two_vehicles_dict[key] = []  # vehicle types
    #         with open('vehicle data.csv', newline='', encoding="utf-8-sig") as csvfile:
    #             reader = csv.DictReader(csvfile)
    #
    #             for row in reader:
    #                 if key == row['record_id']:
    #                     two_vehicles_dict[key].append(row['Vehicle type'])
    #
    # for k, v in two_vehicles_dict.items():
    #     print(k, v)
    # with open('two vehicles types.csv', 'w') as f:
    #     for key, value in two_vehicles_dict.items():
    #         f.write("%s,%s\n" % (key, value))
    #
    # two_vehicles_list = list(two_vehicles_dict.values())
    # for v_list in two_vehicles_list:
    #     v_list.sort()
    #
    # with open('two vehicles count.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',')
    #     two_veh_ctr_dict = dict(Counter(map(tuple, two_vehicles_list)))
    #     for k, v in two_veh_ctr_dict.items():
    #         writer.writerow([k[0], k[1], v])

    # MULTIPLE VEHICLES
    # multiple_vehicles_dict = dict()
    # for key, value in crash_count.items():
    #     if value > 2:
    #         multiple_vehicles_dict[key] = []  # vehicle types
    #         with open('vehicle data.csv', newline='', encoding="utf-8-sig") as csvfile:
    #             reader = csv.DictReader(csvfile)
    #
    #             for row in reader:
    #                 if key == row['record_id']:
    #                     multiple_vehicles_dict[key].append(row['Vehicle type'])
    #
    # # for k, v in multiple_vehicles_dict.items():
    # #     print(k, v)
    #
    # with open('multiple vehicles types.csv', 'w') as f:
    #     for key, value in multiple_vehicles_dict.items():
    #         f.write("%s,%s\n" % (key, value))
    #
    # multiple_vehicles_list = list(multiple_vehicles_dict.values())
    # for v_list in multiple_vehicles_list:
    #     v_list.sort()
    #
    # with open('multiple vehicles count.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',')
    #     multiple_veh_ctr_dict = dict(Counter(map(tuple, multiple_vehicles_list)))
    #     for k, v in multiple_veh_ctr_dict.items():
    #         writer.writerow([k, v])

    # TWO VEHICLES WITH COLLISION TYPE
    # collision_types = ['Angle (Other)', 'Head on', 'Hit object in road', 'Hit parked vehicle', 'Hit pedestrian',
    #                    'Other (see description)', 'Overturned vehicle', 'Rear end', 'Right angle', 'Side swipe', '']
    # v_type_combinations = []
    # with open('vehicle type data.csv', newline='', encoding="utf-8-sig") as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         v_type_combinations.append(tuple(row))
    #
    # count_dict = dict()
    # for v_type_comb in v_type_combinations:
    #     count_dict[v_type_comb] = dict()
    #     for collision_type in collision_types:
    #         ctr = 0
    #
    #         with open('collision type data.csv', newline='', encoding="utf-8-sig") as csvfile:
    #             reader = csv.reader(csvfile)
    #
    #             for row in reader:
    #                 if sorted([row[1], row[2]]) == sorted(list(v_type_comb)) and row[3] == collision_type:
    #                     # print(v_type_comb, row[1], row[2])
    #                     ctr += 1
    #         count_dict[v_type_comb][collision_type] = ctr
    #
    # with open('collision type count.csv', 'w') as f:
    #     for v_type_comb, collision_type_dict in count_dict.items():
    #         for collision_type, count in collision_type_dict.items():
    #             f.write("%s,%s,%s\n" % (v_type_comb, collision_type, count))


if __name__ == '__main__':
    main()
