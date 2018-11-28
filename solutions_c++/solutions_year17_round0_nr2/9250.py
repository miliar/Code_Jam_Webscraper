#include<iostream>
#include<string>
using namespace std;

int check(int s)
{
	int digit[20] = { -1 };
	int d = 0;
	int temp = s;
	while (temp > 0){
		digit[d] = temp % 10;
		temp = temp / 10;
		d++;
	}
	bool flag = true;
	for (int i = 0; i < d - 1; i++){
		if (flag == false)
			break;
		if (digit[i] < digit[i + 1])
			flag = false;
	}
	if (flag == true)
		return s;
	else
	{
		s -= 1;
		check(s);
	}
}

int main()
{
	int t;
	cin >> t;
	for (int k = 1; k <= t;++k){
		long long s;
		cin >> s;
		if ((s % 10) == s)
			cout << "Case #" << k << ": " << s << endl;
		else
			cout << "Case #" << k << ": " << check(s)<<endl;
	}
	return 0;
}