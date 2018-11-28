#include <iostream>
#include <fstream>
#include <cmath>
#include <ctype.h>
using namespace std;
/*
string flipconsk(string line,int i,int k){
    for(int j =0;j<=k;j++){
if(line.at(i+j)=='-'){
    line.at(i+j)='+';

    }else if(line.at(i+j)=='+'){
            line.at(i+j)='-';

        }

    }
    return line;
}*/

int main()
{
string line;
ifstream cin("D:\\Downloads\\final_l.in");
ofstream file("D:\\Downloads\\out.out");
int test ;
cin>>test;
int case_no =1;
getline(cin,line);


outer:
for(; test >=1;--test){

getline(cin,line);

if(line.empty()){
	return 0;
}

//finding k
int pos =line.find(" ");
int k =stoi(line.substr(pos,line.length()));
cout<<k<<" ";
int ender = line.length()-pos;
cout<<ender<<"  }";
    int moves =0;
for(int i =0;i<(line.length()-ender);i++){
        int l =line.length()-(ender+k-1);
    if(i<l){
        if(line.at(i)=='-'){

            for(int j =0;j<k;j++){
                if(line.at(i+j)=='-'){
                    line.at(i+j)='+';

                    }else if(line.at(i+j)=='+'){
                            line.at(i+j)='-';

              }
    }

            moves++;
        }
}
else if(line.at(i)=='-'){
        file <<"Case #"<<case_no<<": IMPOSSIBLE"<<"\n" ;
            cout<<"Case #"<<case_no<<": IMPOSSIBLE"<<"\n" ;
case_no++;
            goto outer;
        }

    }

file <<"Case #"<<case_no<<": "<<moves<<"\n";
cout<<"Case #"<<case_no<<": "<<moves<<"\n" ;
case_no++;



}
file.close();

return 0;
}


