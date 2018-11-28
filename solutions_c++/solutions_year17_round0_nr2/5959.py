#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	char n[20];
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("tidylarge.txt");
	in>>t;
	for(int i=1;i<=t;i++){
		in>>n;
		int len = strlen(n);
		int br=0;
		for(int j=0;j<len-1;j++){
			if(n[j]>n[j+1]){
				br=j;
				n[j] = n[j]-1;
				for(int l=j+1;l<len;l++){
					n[l]='9';
				}
				break;
			}
		}

		for(int j=br;j>0;j--){
			if(n[j]<n[j-1]){
				n[j]='9';
				n[j-1] = n[j-1]-1;
				//cout<<"n[j-1]"<<n[j-1]<<endl;
			}
		}
		int k=0;
		int flag=0;
		for(int j=0;j<len;j++){
			if(flag){
				n[k++]=n[j];
			}else{
				if(n[j]!='0'){
					n[k]=n[j];
					flag=1;
					k++;
				}
			}
		}
		n[k]='\0';

		out<<"Case #"<<i<<": "<<n<<endl;

	}
	return 0;
}