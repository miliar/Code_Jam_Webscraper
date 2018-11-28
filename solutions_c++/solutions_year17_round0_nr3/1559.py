#include<bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;


    long long int n,k,f,s,i,j;

	for (int test = 1; test <= t; ++test)
	{
        map <long long int,long long int > m;
        map<long long int,long long int>::iterator rit;

        cin>>n;
        cin>>k;

        m[n]=1;


        while(k>0 ){
            rit=m.end();
            rit--;
            f=rit->first;
            s=rit->second;
            if(f==0){
                break;
            }
            m.erase(rit);
            if(f%2==1){
                m[f/2]+=2*s;
                i=f/2;
                j=f/2;
            }
            else{
                m[f/2]+=s;
                m[ (f/2) -1]+=s;
                i=f/2;
                j=f/2-1;
            }

            k=k-s;
            //cout<<f<<" "<<k<<endl;
        }

        cout<<"Case #"<<test<<": "<<i<<" "<<j<<endl;

	}


	return 0;
}
