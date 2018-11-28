#include<iostream>
#include <string> 

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("C.txt","w",stdout);
	int t;
	cin>>t;

	int p=1;

	while(p<=t){
		long long n;
		cin>>n; 

		if(n>=0 && n<=9){
			cout<<"Case #"<<p<<": "<<n<<endl;
			p++;
			continue;
		}

		string temp =to_string(n);
		int i;
		int y=0;
			for (i = 1; i < temp.length(); i++) {
                 if (temp[i] < temp[i-1]) 
                { y=1;
                	break;}
            }

            if(y==1){
            temp[i-1] = temp[i-1]-1;
            for(int j=i;j<temp.length();j++)
            	temp[j] = '9';

            for(int j=i-1;j>0;j--){
            	if(temp[j]<temp[j-1]){
            		temp[j-1] = temp[j-1]-1;
            		temp[j] = '9';
            	}
            }
        }

            cout<<"Case #"<<p<<": ";
            int q=0;
            while(temp[q]=='0')
            	q++;

            for(int k=q;k<temp.length();k++)
            	cout<<temp[k];

            cout<<endl;
            p++;

	}
}