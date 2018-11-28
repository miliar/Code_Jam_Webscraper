#include <bits/stdc++.h>
using namespace std;

void change(string &str, int &i, int &k) {
	  for(int j=i;j<i+k;j++)
			{
                if(str.at(j)=='+')
                    str.at(j)='-';
                else
                    str.at(j)='+';
    		}
}

int main()
{
 	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int j=1;j<=t;j++){
    string str;
    int k;
    cin>>str;
    cin>>k;
    int i=0;
    int len=str.length();

//cout<<str<<" len: "<<len<<" "<<k<<" :-"<<endl;
    size_t found = str.find('-');
  	if (found==std::string::npos) {
  		cout<<"Case #"<<j<<": 0"<<endl;
  		continue;
	  }
    int count=0;
    while (i+k<=len) {
    	if (str[i]=='-') {
    		change(str,i,k);
    		count++;
    		//cout<<"after change: i="<<i<<" k="<<k<<" len="<<len<<endl;
    		i++;
		}
		else {
			i++;
		}
	}
	int flag=0;
	while(i<=len) {
		if (str[i]=='-') {
			cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
			//cout<<str<<" IMPOSSIBLE"<<endl;
			flag++;
			break;
		} 
		else {
			i++;
		}
	}
	
	if (flag==0)
	cout<<"Case #"<<j<<": "<<count<<endl;
    //cout<<str<<" possible"<<endl;
   }

   return 0;
}
