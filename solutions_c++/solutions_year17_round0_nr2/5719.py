#include<bits/stdc++.h>
using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)


int main(){

	int T;
	scanf("%d ", &T);

	f(t,1,T)
	{
		cout<<"Case #"<<t<<": ";


		long long n;
		cin>>n;
		

		vector<long long> v, u, resp;
		v.clear(); u.clear(); resp.clear();
		for(; n>0;n/=10)
			u.push_back(n%10);

		int tam = u.size();

		for(int i=0;i<tam ;i++)
			v.push_back(u[tam-1-i]);

		// for(int i=0; i<tam; i++)
		// {
		// 	cout<<v[i];
		// }
		// cout<<endl;


		int i;
		for(i=0; i<tam-1; i++) // ate o penultimo
		{
			if(v[i]>v[i+1])	
				break;
		}

		if(i==tam-1){
			for(int j=0; j< tam; j++){
				cout<<v[j];
			}
			cout<<endl;
		}
		else{
			int j;
			for(j=i;j>=0; j--)
			{
				if(v[j]!=v[i]){
					j++;
					break;
				}
			}
			j = max(j, 0);
			
			for(int k=0; k<=j-1; k++)
			{
				resp.push_back(v[k]);
			}
			
			resp.push_back(v[j]-1);
			
			for(int k=j+1; k<tam; k++)
				resp.push_back(9);
			
			
			bool flag = false;
			for(int i=0; i<resp.size(); i++)
			{
				if(resp[i]!=0)
					flag = true;
				if(flag)
					cout<<resp[i];

			}
			cout<<endl;
			
		}
			
	}


	return 0;
}