#include<iostream>
#include<vector>
using namespace std;

struct horse {
	long long init_pos;
	long long max_speed;
};

double get_cruise_control(long long dest, vector<horse>& horses) {
	double max_req_time = (double)(dest-horses[0].init_pos)/horses[0].max_speed;
	double req_time;
	for(int i = 1; i < horses.size(); i++) {
		req_time = (double)(dest-horses[i].init_pos)/horses[i].max_speed;
		if(req_time > max_req_time) {
			max_req_time = req_time;
		}
	}
	return dest/max_req_time;	
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)	{
		vector<horse> horses;
		long long D, K, S;
		int N;
		cin >> D >> N;
		for(int j = 0; j < N; j++) {
			cin >> K >> S;
			horse h;
			h.init_pos = K;
			h.max_speed = S;
			horses.push_back(h);
		}
		cout.precision(6);
		cout << "Case #" << i << ": " << fixed << get_cruise_control(D, horses) << endl;
	}
	return 0;
}