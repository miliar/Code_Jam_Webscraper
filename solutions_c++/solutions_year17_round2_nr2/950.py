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
static char color[] = "ROYGBV";

std::string func(int total_num, vector<int> color_cnt, bool small_set = true) {
	string ans = "";
	if (small_set) {
		if (color_cnt[0] > color_cnt[2] + color_cnt[4] || color_cnt[2] > color_cnt[0] + color_cnt[4] || color_cnt[4] > color_cnt[2] + color_cnt[0])
			return "IMPOSSIBLE";
		else {
			int max_cnt = (color_cnt[0] > color_cnt[2]) ? 0 : 2;
			max_cnt = (color_cnt[max_cnt] > color_cnt[4]) ? max_cnt : 4;
			int idx = max_cnt;
			int last_assigned = -1;
			for (int i = 0; i < total_num; i++) {
				if (color_cnt[idx] > 0) {
					ans += color[idx];
					color_cnt[idx] --;
					last_assigned = idx;
					int cd1 = (idx + 2) % 6;
					int cd2 = (idx + 4) % 6;
					if (color_cnt[cd1] == color_cnt[cd2]) {
						if (cd1 == max_cnt)
							idx = cd1;
						else
							idx = cd2;
					}
					else
						idx = color_cnt[cd1] > color_cnt[cd2] ? cd1 : cd2;
				}
			}
		}//small_set
	}
	else
	{
		if (total_num == (color_cnt[1] + color_cnt[4])) {
			if (color_cnt[4] == color_cnt[1]) {
				for (int i = 0; i < total_num / 2; i++) {
					ans += "OB";
				}
				return ans;
			}
			else
			{
				return "IMPOSSIBLE";
			}
		}
		if (total_num == (color_cnt[3] + color_cnt[0])) {
			if (color_cnt[3] == color_cnt[0]) {
				for (int i = 0; i < total_num / 2; i++) {
					ans += "RG";
				}
				return ans;
			}
			else
			{
				return "IMPOSSIBLE";
			}
		}

		if (total_num == color_cnt[5] + color_cnt[2]) {
			if (color_cnt[5] == color_cnt[2]) {
				for (int i = 0; i < total_num / 2; i++) {
					ans += "YV";
				}
				return ans;
			}
			else
			{
				return "IMPOSSIBLE";
			}
		}

		color_cnt[0] -= color_cnt[3];
		color_cnt[2] -= color_cnt[5];
		color_cnt[4] -= color_cnt[1];
		if (color_cnt[0] < 0 || color_cnt[2] < 0 || color_cnt[4] < 0) {
			return "IMPOSSIBLE";
		}
		int RYB_cnt = color_cnt[0] + color_cnt[2] + color_cnt[4];

		if (color_cnt[0] > color_cnt[2] + color_cnt[4] || color_cnt[2] > color_cnt[0] + color_cnt[4] || color_cnt[4] > color_cnt[2] + color_cnt[0])
			return "IMPOSSIBLE";
		else {
			int max_cnt = (color_cnt[0] > color_cnt[2]) ? 0 : 2;
			max_cnt = (color_cnt[max_cnt] > color_cnt[4]) ? max_cnt : 4;
			int idx = max_cnt;
			for (int i = 0; i < RYB_cnt; i++) {
				if (color_cnt[idx] > 0) {
					ans += color[idx];
					color_cnt[idx] --;
					int cd1 = (idx + 2) % 6;
					int cd2 = (idx + 4) % 6;
					if (color_cnt[cd1] == color_cnt[cd2]) {
						if (cd1 == max_cnt)
							idx = cd1;
						else
							idx = cd2;
					}
					else
						idx = color_cnt[cd1] > color_cnt[cd2] ? cd1 : cd2;
				}
			}
		}
		if (color_cnt[1]>0) {

			size_t blue_idx = ans.find("B");
			if (blue_idx == string::npos) return"IMPOSSIBLE";
			for (int i = 0; i < color_cnt[1]; i++) {
				ans.insert(blue_idx, 1, 'O');
				ans.insert(blue_idx, 1, 'B');
			}

		}
		if (color_cnt[3]>0) {

			size_t red_idx = ans.find("R");
			if (red_idx == string::npos) return"IMPOSSIBLE";
			for (int i = 0; i < color_cnt[3]; i++) {
				ans.insert(red_idx, 1, 'G');
				ans.insert(red_idx, 1, 'R');
			}
		}
		if (color_cnt[5]>0) {
			size_t yellow_idx = ans.find("Y");
			if (yellow_idx == string::npos) return"IMPOSSIBLE";
			for (int i = 0; i < color_cnt[5]; i++) {
				ans.insert(yellow_idx, 1, 'V');
				ans.insert(yellow_idx, 1, 'Y');
			}
		}
	}
	return ans;
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

	fscanf(inf, "%d", &case_count);

	int cnt, i;

	vector<int> color_cnt;
	int tmp_cnt, total;

	for (cnt = 1; cnt < case_count + 1; cnt++) {

		fscanf(inf, "%d", &total);

		color_cnt.clear();
		for (i = 0; i < 6; i++) {

			fscanf(inf, "%d", &tmp_cnt);
			color_cnt.push_back(tmp_cnt);
		}

		fprintf(of, "Case #%d: %s \n", cnt, func(total, color_cnt, false).c_str());

	}
	fclose(inf);
	fclose(of);

	return 0;
}
