#include <iostream>
using namespace std;
int main()
{
	int T, x, j;
	long long int N, y, i, pos;
	cin >> T;
	for(x=1; x<=T; x++)
	{
		cin >> N;
		y=0;
		pos=1;
		i=N%10;
		while(N>0)
		{
			N/=10;
			j=N%10;
			if(i==0 || i<j)
			{
				N--;
				j=N%10;
				for(i=1, y=0; i<=pos; i*=10)
					y+=9*i;
			}
			else
				y+=i*pos;
			pos*=10;
			i=j;
		}
		cout << "Case #" << x << ": " << y << endl;
	}
	return 0;
}