#include<stdio.h>
#include<vector>

namespace {
	using std::vector;
	
	double calculate(vector<double>& distances, vector<double>& max_distances, vector<double>& speeds) {
		vector<double> times(speeds.size());
		times[times.size()-1] = 0;
		for (int j = times.size()-2;j >= 0;--j) {
			times[j] = -1;
			for (int k = j+1;k < times.size() && max_distances[j] >= distances[k] - distances[j];++k) {
				if (times[j] == -1 || times[j] > times[k] + (distances[k] - distances[j])/speeds[j]) {
					times[j] = times[k] + (distances[k] - distances[j])/speeds[j];
				}
			}
		}
		return times[0];
	}
}

int main(int argc, char** argv) {
	if (argc != 3) return 0;
	FILE* input;
	FILE* output;
	input = fopen(argv[1],"r");
	output = fopen(argv[2],"w");
	int t;
	fscanf(input,"%d",&t);
	for (int z = 0;z < t;++z) {
		int n; int q;
		fscanf(input,"%d",&n);
		fscanf(input,"%d",&q);
		vector<double> speeds; vector<double> max_distances;
		for (int i = 0;i < n;++i) {
			int distance; int speed;
			fscanf(input,"%d",&distance);
			max_distances.push_back(distance);
			fscanf(input,"%d",&speed);
			speeds.push_back(speed);
		}
		vector<double> distances;
		distances.push_back(0.0);
		for (int i = 0;i < n;++i) {
			for (int j = 0;j < n;++j) {
				int distance;
				fscanf(input,"%d",&distance);
				if (distance > 0) {
					distances.push_back(distances[distances.size()-1] + distance);
				}
			}
		}
		int i; int j; fscanf(input,"%d",&i); fscanf(input,"%d",&j);
		double ans = calculate(distances,max_distances,speeds);
		fprintf(output,"Case #%d: %lf \n",z+1,ans);
	}
}
