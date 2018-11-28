#include <bits/stdc++.h>
using namespace std;

int count=0,bp;
string temp2="";

void f(){
    //cout<<"temp2 "<<temp2<<endl;
    int i,len=temp2.size();
    i=len-1;
    if(len==1){
        return;
    }
    while(i>0){
        if(temp2[i]<temp2[i-1]){
            ::count+=len-i;
            temp2[i-1]-=1;
            bp=i-1;
            string temp3="";
            for(i=0;i<=bp;i++)
                temp3+=temp2[i];
            temp2=temp3;
            f();
            return;

        }
        i--;
    }
    return;
}
int main(){
	long long tc,len,n,j=0,i;
	string temp;
	fstream fin;
	fstream fout;
	fin.open("input.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>temp;

	stringstream convert(temp);//object from the class stringstream
	convert>>tc;

	while(j<tc){
		fin>>temp;
		//cout<<temp<<endl;
		//stringstream convert(temp);//object from the class stringstream
		//convert>>n;

		len=temp.size();

		if(len!=1){
            for(i=0;i<len;i++){
                if(temp[i]=='0'){
                    ::count+=len-i;
                    break;
                }
            }
            bp=i-1;
            if(::count!=0)
                temp[i-1]=temp[i-1]-1;
            for(i=0;i<=bp;i++)
                temp2+=temp[i];

            f();

            temp="";
            for(i=1;i<=::count;i++){
                temp2+='9';

            }
            for(i=0;i<temp2.size();i++){
                if(temp2[i]=='0'){
                    continue;
                }
                else{
                    temp+=temp2[i];
                }
            }
        }
		fout<<"Case #"<<j+1<<": "<<temp<<endl;
		j++;
        temp2="";
        ::count=0;
	}
	return 0;
}
