
#ifdef WIN32
#pragma warning(disable:4996)
#pragma warning(disable:4819)
#pragma warning(disable:4101)
#endif

#include <stdio.h>
#include <math.h>

#include <vector>
using namespace std;

bool check(const vector<int> &d){
	for (int i = 0; i < d.size(); i++){
		if (d[i] == 0) return false;
	}
	return true;
}

int calc(const vector<int> &d, const int k){
	if (check(d) == true){
		return 0;
	}

	const int length = d.size() + 1 - k;
	const int num = (int)(pow(2, length) + 0.5);

	int min = length + 1;

	vector<int> cand(length);
	for (int c = 0; c < num; c++){

		int cnt = 0;
		for (int i = 0; i < length; i++){
			const int v = ((c >> i) & 1) ? 1 : 0;
			cand[i] = v;
			cnt += v;
		}
		if (cnt >= min) continue;

		vector<int> tmp = d;

		// flip
		for (int i = 0; i < length; i++){
			if (cand[i] > 0){
				for (int j = i; j < i + k; j++){
					tmp[j] = 1 - tmp[j];
				}
			}
		}

		if (check(tmp) == true){
			min = cnt;
		}
	}

	return (min < length + 1) ? min : -1;
}

int main(){

	int num;
	vector<int> K;
	vector<vector<int>> data;

	FILE *fp;

	fp = fopen("A-small-attempt1.in", "r");
	
	fscanf(fp, "%d\n", &num);
	for (int i = 0; i < num; i++){
		vector<int> d;
		int k;

		int c;
		while ((c = fgetc(fp)) != ' '){
			d.push_back((c == '+') ? 1 : 0);
		}
		fscanf(fp, "%d\n", &k);

		data.push_back(d);
		K.push_back(k);
	}
	
	fclose(fp);


	fp = fopen("result.txt", "w");
	for (int i = 0; i < num; i++){
		const int result = calc(data[i], K[i]);

		if (result >= 0){
			fprintf(fp, "Case #%d: %d\n", i + 1, result);
		}
		else{
			fprintf(fp, "Case #%d: %s\n", i + 1, "IMPOSSIBLE");
		}
	}
	fclose(fp);

	return 0;
}