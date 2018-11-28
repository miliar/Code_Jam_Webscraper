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

	string s;
	unsigned long long int n,m=0,pre,val,p;

	for (int test = 1; test <= t; ++test)
	{

        cin>>s;
        n=s.length();
        int flag=0;
        p=pow(10,(n-1) ) ;
        m= (s[0]-'0');

        int j=1;
        while(j<=n-1){
            m=m*10;
            j++;
        }

        pre=(s[0]-'0');
        val=(s[0]-'0');

        //cout<<m<<" "<<(s[0]-'0')*(pow(10,(n-1) ) )<<" ";

        for(int i=1;i<s.length();i++){

            if( (s[i]-'0')> pre ){
                val=val*10+(s[i]-'0');
                pre=s[i]-'0';
                flag=0;

                m=val;
                int j=1;
                while(j<s.length()-i){
                    m=m*10;
                    j++;
                }

            }
            else if( (s[i]-'0')== pre ){
                flag=1;
                val=val*10+(s[i]-'0');
                pre=s[i]-'0';
            }
            else{


                int j=1;
                while(j<=s.length()-i){
                    val=val*10;
                    j++;
                }

                val--;
                if(flag==1){
                    val=m-1;
                }
                break;
            }
            //cout<<val<<" "<<m<<endl;
        }



		cout<<"Case #"<<test<<": "<<val<<endl;
	}



	return 0;
}
