#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

struct data{
	int radius;
	int height;
	double area;
};

bool acompare(data a, data b) {
	if (a.radius > b.radius) {
		return true;
	}
	else if (a.radius == b.radius) {
		return a.area < b.area;
	}
	else return false;
}

bool area(data a, data b) {
	return a.area > b.area;
}


double max_total_area;

void fact(data *arr, int n, int k, int current, int selected, double total_area, vector<int> selected_array) {
	if (selected==k) {
		if (total_area > max_total_area) {
			max_total_area = total_area;

			// cout << "NEW BIGGEST " << total_area << endl;
			// for (int i=0; i<selected_array.size(); i++) {
			// 	cout << arr[selected_array[i]].radius << " " << arr[selected_array[i]].height << " " << arr[selected_array[i]].area << endl;
			// }
			// cout << "END NEW BIGGEST" << endl;
			// cout << endl;
		}
	}
	else {
		for (int i=current; i<n; i++) {
			if (selected==0 || arr[i].radius <= arr[selected_array[selected_array.size()-1]].radius ) {
				int local_selected = selected+1;
				double local_total_area = total_area;
				if (selected>0)
					local_total_area += arr[i].area - ((double)arr[i].radius * (double)arr[i].radius);
				else local_total_area += arr[i].area;

				vector<int> selected_array_clone = selected_array;
				selected_array_clone.push_back(i);
				fact(arr, n, k, i+1, local_selected, local_total_area, selected_array_clone);
			}
		}
	}
}

int main() {
	int t;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {
		int n, k;
		scanf("%d %d",&n, &k);

		data arr[n];
		for (int i=0; i<n; i++) {
			scanf("%d %d",&arr[i].radius, &arr[i].height);
			arr[i].area = ((double)arr[i].radius * (double)arr[i].radius) + (2.0 * (double)arr[i].radius * (double)arr[i].height);
		}

		// if (k==n) {
		sort(arr, arr+n, acompare);
		// }
		// else sort(arr, arr+n, area);
		// sort(arr, arr+n, area);

		
		//greedy strategy
		// double max_total_area = -1;
		// for (int initial=0; initial<n; initial++) {

		// 	double total_area = 0;
		// 	int selected = 0;
		// 	int prev_rad = -1;
		// 	double prev_surface = 0.0;

		// 	for (int i=initial; i<n; i++) {
		// 		if (i==initial || arr[i].radius <= prev_rad) {
		// 			selected++;
		// 			if (i>initial)
		// 				total_area += arr[i].area - ((double)arr[i].radius * (double)arr[i].radius);
		// 			else total_area += arr[i].area;

		// 			prev_rad = arr[i].radius;
		// 		}

		// 		if (selected==k) {
		// 			break;
		// 		}
		// 	}

		// 	// cout << total_area << endl;
		// 	if (total_area > max_total_area) {
		// 		max_total_area = total_area;
		// 	}
		// }

		max_total_area = -1.0;
		vector<int> temp;
		fact(arr, n, k, 0, 0, 0.0, temp);

		printf("Case #%d: %.9lf\n",z, max_total_area * M_PI);
		// cout << "Case #" << z << ": " << total_area << " " << total_area * M_PI << endl;
	}
	return 0;
}