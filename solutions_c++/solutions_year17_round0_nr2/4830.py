#include<iostream>
#include<string>

using namespace std;

long long solution(long long a)
{
	string num = to_string(a);
	int n = num.size();
	num.insert(0, "0");
	num.push_back('9');
	int i;
	for(i = 1; i <= n;)
	{
		if(num[i] <= num[i+1])
			i++;
		else{
			while(--num[i] < num[i-1])
				i--;
			break;
		}
	}
	while(++i <= n)
		num[i] = '9';
	num.pop_back();
	return stoll(num);

} 

int main()
{
	long long t, n;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> n;
		cout << "Case #" << i << ": " << solution(n) << endl;
	}
	return 0;

}
