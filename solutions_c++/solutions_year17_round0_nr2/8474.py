
#ifdef WIN32
#pragma warning(disable:4996)
#pragma warning(disable:4819)
#pragma warning(disable:4101)
#endif

#include <stdio.h>
#include <math.h>

#include <vector>
using namespace std;

vector<int> calc(vector<int> &d){
	vector<int> result;

	for (int i = 0; i < d.size(); i++){
		if (i == d.size() - 1){
			result.push_back(d[i]);
			continue;
		}

		bool flag = true;
		for (int j = i + 1; j < d.size(); j++){
			if (d[j] < d[i]){
				flag = false;
				break;
			}
			else if (d[j] > d[i]){
				flag = true;
				break;
			}
		}
		
		if (flag == true){
			result.push_back(d[i]);
		}
		else{
			if (d[i] > 1){
				result.push_back(d[i] - 1);
			}
			for (int j = i + 1; j < d.size(); j++){
				result.push_back(9);
			}
			break;
		}
	}

	return result;
}

int main(){

	int num;
	vector<vector<int>> data;

	FILE *fp;

	fp = fopen("B-large.in", "r");
	
	fscanf(fp, "%d\n", &num);
	for (int i = 0; i < num; i++){
		vector<int> d;

		int c;
		while ((c = fgetc(fp)) != '\n'){
			d.push_back(c - '0');
		}

		data.push_back(d);
	}
	
	fclose(fp);


	fp = fopen("result.txt", "w");
	for (int i = 0; i < num; i++){
		const vector<int> result = calc(data[i]);

		fprintf(fp, "Case #%d: ", i + 1);
		for (int i = 0; i < result.size(); i++){
			if(result[i] == 0) continue;
			fprintf(fp, "%d", result[i]);
		}
		fprintf(fp, "\n");
	}
	fclose(fp);

	return 0;
}