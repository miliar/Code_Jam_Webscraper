#include "iostream"
#include "vector"

using namespace std;

int checkTidy(char*a)
{
	int position = 0;
	
	while (a[position] != '\0') {
		if (a[position + 1] != '\0')
		{
			if ((a[position + 1] - 48) >= (a[position] - 48)) position++;
			else return position + 1;
		}
		else
			break;
	}
	if (a[position + 1] == '\0')   return 99;
	else
		return position;

}
void makeTidy(char*a, int pos) {
	a[pos - 1] = (a[pos - 1] - 48 - 1)+ 48;
	while (a[pos] != '\0') {
		a[pos] = '9';
		pos++;
	}
}
void check_maketTidy(char *a)
{
	int p = checkTidy(a);
		if (p ==99)
			return;
		else {
			makeTidy(a,p);
			check_maketTidy(a);
		}
	    	
}
void integertoa(unsigned long long int n, char* a)
{
	char temp[19];
	int iter = 0;
	while (n/10>=1)
	{
		temp[iter] = (n % 10) + 48;
		iter++;
		n = n / 10;
	}
	temp[iter] = n+48;
	a[iter + 1] = '\0';
	int i = 0;
	while (iter >= 0)
	{
		a[i++] = temp[iter--];
	}
	
}
int main() {
	int T;
    unsigned long long int N;
	char aNumber[200];
	
	
	//freopen("B-large.in", "r", stdin);
	//freopen("outputLargeB.txt", "w", stdout);
	cin >> T;
	int C = T;
	while (T--)
	{
		cin >> N;
		integertoa(N, aNumber);
		check_maketTidy(aNumber);

		//check and delete leading zero
		int i = 0;
		while (aNumber[i] != '\0') {
			if (aNumber[i] == '0') i++;
			else break;
		}
			cout << "Case #" << C-T << ": " << &aNumber[i] << endl;
	}
	return 0;
}