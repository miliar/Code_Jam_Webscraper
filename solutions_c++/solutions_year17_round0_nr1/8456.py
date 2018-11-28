#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
/*
ifstream inf("C://Users//jungwoong//Desktop//new//A-small-attempt0.in");
ofstream onf("C://Users//jungwoong//Desktop//new//output.txt");*/
char arr[100][1000];
int pen[100];
void find(char now[], int p) {
	int len = strlen(now);
	char temp;
	int ans = 0;
//	cout << "°£´Ù!" << ' ';
	for (int i = 0; i < len - p+1; i++) {
//		printf("%c", now[i]);
		if (now[i] == '-') {
			ans++;
			for (int j = i; j < p+i; j++) {
				if (now[j] == '-') {
					now[j] = '+';
				}
				else {
					now[j] = '-';
				}
			}
		}
	}
	for (int i = len - p; i < len; i++) {
		if (now[i] == '-') {
			ans = -1;
			break;
		}
	}
//	cout << " ³¡ " << endl;
	if (ans == -1) {
		printf("IMPOSSIBLE\n");
	}
	else {
		printf("%d\n", ans);
	}

}   

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int num = 0;
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%s ", arr[i]);
		scanf("%d\n", &pen[i]);
	}
//	cout << num;

	int no = 0;
	for (int i = 0; i < num; i++) {
		printf("%s %d \n", arr[i], pen[i]);
		no = i + 1;
		printf("Case #%d: ", no);
		find(arr[i], pen[i]);
//		cout << arr[i] << ' ' << pen[i] << endl;
	}
	/*inf.close();
	onf.close();*/
	return 0;
}