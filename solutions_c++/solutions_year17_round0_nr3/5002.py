#include <iostream>
#include <queue>

using namespace std;



int main()
{

int T,N,K,s_l,s_r,a;

cin >> T;

for(int i=0; i<T; i++)
{

priority_queue <int> vaccant;
	cin >> N >> K;

	vaccant.push(N);


	for(int j=0; j<K; j++)
	{

		a = vaccant.top();
		vaccant.pop();

		if(a%2==0)
		{
			s_l = a/2 - 1;
			s_r = a/2;
		}

		else
		{
			s_l = (a-1)/2;
			s_r = s_l;
		}


		
		if(s_r!=0)
		{
			//cout<< s_r  << "   ";
			vaccant.push(s_r);
		}
		if(s_l!=0)
		{
			//cout<< s_l << endl;
			vaccant.push(s_l);
		}

		
	}

cout<< "Case #" << i+1 << ": "<< s_r << "  " << s_l << endl;

}


}