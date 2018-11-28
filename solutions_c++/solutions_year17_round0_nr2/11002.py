#include <bits/stdc++.h>
using namespace std;
long long int best(long long int input)
{
    long long int num = input;
repeat:
	while(input >= 10){
		if((input % 10 < ((input % 100) / 10)) || (input % 10 == 0 && input > 9)){
			num--;
			input = num;
			goto repeat;
		}
		input /= 10;
	}
	return num;
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
    int tc,cs=1;
    cin >> tc;
    while(tc--)
    {
   		int number;
   		cin >> number;
   		cout << "Case #" << cs++ << ": " << best(number) << endl;
    }
    return 0;
}
