//  Created by Luna_Z on 17/4/6.
//  Copyright © 2017 Luna_Z. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include "math.h"
using namespace std;

static int case_count;
char const* input_path = "C:\\Users\\Luna\\Desktop\\input.in";
char const* output_path = "C:\\Users\\Luna\\Desktop\\output.out";

std::string func(int horse_num, int dest, vector<int> dis, vector<int>spd) {
	double max_t = 0;
	for (int i = 0; i <horse_num; i++) {
		double time = static_cast<double> (dest - dis[i]) / spd[i];
		max_t = fmax(time, max_t);
	}
	double ans = (double)dest / max_t;
	return to_string(ans);
}

int main() {

	//read the input file and pass the arguemnt to function

	FILE *inf = fopen(input_path, "r");
	if (inf == NULL) {
		printf("Could not find input file! \n");
		getchar();
		return 1;
	}

	FILE *of = fopen(output_path, "w");
	if (of == NULL) {
		printf("The path of output file has errors! \n");
		getchar();
		return 1;
	}
	scanf("%d", &case_count);
	//fscanf(inf, "%d", &case_count);

	int cnt, i, j;

	vector<int> dis, spd;
	int tmp_dis, tmp_spd, dest, horse_num;

	for (cnt = 1; cnt < case_count + 1; cnt++) {
		fscanf(inf, "%d", &dest);
		fscanf(inf, "%d", &horse_num);
		dis.clear();
		spd.clear();
		for (i = 0; i < horse_num; i++) {

			fscanf(inf, "%d", &tmp_dis);
			dis.push_back(tmp_dis);

			fscanf(inf, "%d", &tmp_spd);
			spd.push_back(tmp_spd);
		}
		fprintf(of, "Case #%d:\n%s", cnt, func(horse_num, dest, dis, spd).c_str());
	}
	fclose(inf);
	fclose(of);

	return 0;
}
