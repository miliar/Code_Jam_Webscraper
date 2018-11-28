#include <iostream>
#include <vector>

using namespace std;

struct Pancake {
  long long radius;
  long long height;
};

struct compare_rh
{
    inline bool operator() (const Pancake& struct1, const Pancake& struct2)
    {
        return (struct1.radius * struct1.height > struct2.radius * struct2.height);
    }
};

int main() {

	int T;
	double PI = 3.14159265358979323846;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
			int N, K;
			long long sum = 0, max_sum;
			Pancake max_pan;
			vector<Pancake> pancakes, finalpan;
			cin >> N >> K;

			for(int i = 0; i < N; i++) {
				long long ra, he;
				cin >> ra;
				cin >> he;
				Pancake one_pancake = {ra, he};
				pancakes.push_back(one_pancake);
			}

			sort(pancakes.begin(), pancakes.end(), compare_rh());

			// for(int i = 0; i < N; i++) {
			// 	cout << pancakes[i].radius << " ";
			// 	cout << pancakes[i].height;
			// 	cout << endl;
			// }

			max_pan = pancakes[0];
			for(int i = 0; i < K - 1; i++) {
				if(pancakes[i].radius > max_pan.radius) {
					max_pan = pancakes[i];
				}
        long long tmp = 2 * pancakes[i].radius * pancakes[i].height;
        // tmp *= pancakes[i].height;
				// cout << pancakes[i].radius << " " << pancakes[i].height << " " << tmp << endl;
				sum += tmp;
				finalpan.push_back(pancakes[i]);
			}
			// cout << max_pan.radius << " " << sum << endl;
			max_sum = sum;
			for(int i = K - 1; i < N; i++) {
				long long tmp_sum;
				if(pancakes[i].radius <= max_pan.radius) {
          // long long tmp = max_pan.radius;
          // tmp *= max_pan.radius;
          // tmp_sum = sum;
          // tmp_sum += tmp;
          // tmp = 2 * pancakes[i].radius;
          // tmp *= pancakes[i].height;
          // tmp_sum += tmp;
					tmp_sum = sum + max_pan.radius * max_pan.radius + 2 * pancakes[i].radius * pancakes[i].height;
				}
				else {
          // long long tmp = pancakes[i].radius;
          // tmp *= pancakes[i].radius;
          // tmp_sum = sum + tmp;
          // tmp = 2 * pancakes[i].radius;
          // tmp *= pancakes[i].height;
          // tmp_sum += tmp;
					tmp_sum = sum + pancakes[i].radius * pancakes[i].radius + 2 * pancakes[i].radius * pancakes[i].height;
				}
				if(tmp_sum > max_sum)
					max_sum = tmp_sum;
			}

			// cout << max_sum << endl;
			cout << "Case #" << t + 1 << ": ";
			printf("%.9lf\n", (double)PI * max_sum);


			// cout << "Case #" << t + 1 << ": " << endl;
			// for(int i = 0; i < R; i++) {
			// 	for(int j = 0; j < C; j++) {
			// 		cout << array[i][j];
			// 	}
			// 	cout << endl;
			// }

	}
	return 0;
}
