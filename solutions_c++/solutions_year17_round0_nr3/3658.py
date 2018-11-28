#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int power_of_2_less_or_eq_K(long long int K)
{
	int x = 0;
	while(pow((double)2,x)<=K)
	{
		x++;
	}
	return x-1;
}

int main()
{
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++)
	{
		long long int N;
		long long int K;
		cin>>N>>K;
		int x = power_of_2_less_or_eq_K(K);

		long long int elem = N/pow((double)2, x);

		if(elem==1)
		{
			cout<<"Case #"<<tc+1<<": 0 0"<<endl;
		}
		else
		{
			queue<long long int> q;
			map<long long int, long long int> m;
			q.push(N);
			m[N] = 1;

			while(!q.empty())
			{
				long long int v = q.front();
				q.pop();

				if(v&1)
				{
					if(v/2 > 1 && m.find(v/2)==m.end())
						q.push(v/2);

					if(m.find(v/2)!=m.end())
						m[v/2] += 2*m[v];
					else
						m[v/2] = 2*m[v];
				}
				else
				{
					if(v/2-1 > 1 && m.find(v/2-1)==m.end())
						q.push(v/2-1);
					if(v/2 > 1 && m.find(v/2)==m.end())
						q.push(v/2);

					if(m.find(v/2-1)!=m.end())
						m[v/2-1] += m[v];
					else
						m[v/2-1] = m[v];

					if(m.find(v/2)!=m.end())
						m[v/2] += m[v];
					else
						m[v/2] = m[v];
				}
			}

			long long int count_elem_at_level_x = 0;
			if(x==0)
				count_elem_at_level_x = 1;
			else
				count_elem_at_level_x = m[2*elem] + 2*m[2*elem+1] + m[2*elem+2];

			long long int elem_at_this_level = (K- pow((double)2, x) + 1);
			cout<<"Case #"<<tc+1<<": ";
			if(elem_at_this_level <= count_elem_at_level_x)
			{
				if(elem&1)
					cout<<elem/2<<" "<<elem/2<<endl;
				else
					cout<<elem/2<<" "<<elem/2-1<<endl;
			}
			else
			{
				if((elem-1)&1)
					cout<<(elem-1)/2<<" "<<(elem-1)/2<<endl;
				else
					cout<<(elem-1)/2<<" "<<(elem-1)/2-1<<endl;
			}
		}
	}
	return 0;
}