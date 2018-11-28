#include <iostream>
#include <fstream>
using namespace std;
ifstream inf("C://Users//jungwoong//Desktop//new//B-large.in");
ofstream onf("C://Users//jungwoong//Desktop//new//output.txt");
char arr[100][20];
int number[20];
void find(char now[]) {
	int len = strlen(now);
	int temp=0;
	int t = 0;
	for (int i = 0; i < len; i++) {
		number[i] = now[i]-48;
//		cout << number[i];
	}
//	cout << ' ' << len << endl;
	while (true) {
		for (int i = len - 1; i > 0; i--) {
			if (number[i - 1] > number[i] || number[i] == 0) {
				t++;
				number[i] = 9;
				temp = i - 1;
				for (int j = i; j < len ; j++) {
					number[j] = 9;
				}
				while (true) {
					if (number[temp] == 0) {
						number[temp] = 9;
						temp--;
					}
					else {
						number[temp]--;
						break;
					}		
				}
			}
		}
		if (t == 0)
			break;
		else
			t = 0;
	}
	temp = 0;
	if (number[0] == 0) {
		for (int i = 1; i < len; i++) {
			//printf("%d", number[i]);
			temp = number[i];
			onf << temp;
		}
		onf << endl;
	}
	else {
		for (int i = 0; i < len; i++) {
			temp = number[i];
			onf << temp;
		}
		onf << endl;
	}
	
}

int main() {
	int num = 0;
	int i = 0;
	char numC;

	inf >> num;
	num = atoi(&numC);
	while (inf >> arr[i])
	{
		cout << arr[i] << endl;
		i++;
	}

	int no;
	for (int j = 0; j < i; j++) {
		no = j + 1;
		onf << "Case #" << no << ": " ;
		find(arr[j]);
	}

	inf.close();
	onf.close();
	return 0;
}