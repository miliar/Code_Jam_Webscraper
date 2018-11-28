#include <iostream>
#include <fstream>
using namespace std;

int find_max(int * arr, int size) {
	int max = arr[0];
	int max_index = 0;
	for (int i = 1; i < size; i++) {
		if (arr[i] > max) {
			max = arr[i];
			max_index = i;
		}
	}
	return max_index;
}
int find_max_val(int * arr, int size) {
	int max = arr[0];
	for (int i = 1; i < size; i++) {
		if (arr[i] > max)
			max = arr[i];
	}
	return max;
}
int main() {
	int T;
	cin >> T;
	fstream result;
	result.open("result.txt", ios::out);
	for (int i = 1; i <= T; i++) {
		int x, y;
		cin >> x >> y;
		int left, right;
		int size = y * 2 + 1;
		int * arr = new int[size];
		for (int i = 0; i < size; i++) arr[i] = -1;
		arr[0] = x;
		int counter = 1;
		while (y--) {
			int val = find_max_val(arr, size);
			if (val % 2 == 0) {
				left = val / 2;
				right = val / 2 - 1;
			}
			else {
				left = right = val / 2;
			}
			arr[counter] = right;
			arr[counter + 1] = left;
			counter += 2;
			arr[find_max(arr, size)] = -1;
		}
		result << "Case #" << i << ": " << arr[size - 1] << " " << arr[size - 2] << endl;
		delete[] arr;
	}
	result.close();
	return 0;
}