#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;





int main(){
char S[1003];
int tries;
int T;
bool done;
int K;
int size;
ifstream fin;
ofstream fout ;
fin.open("A-large.in.txt");

fout.open("A1.txt",ios::app);
fin >>T;
for (int num=0;num<T;num++){
done=false;
    for (int m=0;m<1003;m++)
    S[m] = (char)0;
tries=0;

size=0;
fin >> S;
fin >> K;
for (int i=0;i<1003 ;i++)
{

    if (S[i]!=0)
        size++;

}

for (int i=0;i<=size-K && done==false;i++)
{if (S[i]=='-'){
for (int j=i;j<i+K;j++)
{if(S[j]=='+')
   S[j]='-';
   else if (S[j]=='-')
    S[j]='+';


}
    tries++;
}


for(int t=0;t<size ;t++){
            if (S[t]=='-')
{

 done=false;break;}


else if (S[t]=='+')
    done=true;


}

}

if (done==true)
    fout <<"Case #"<<num+1<<": "<< tries<<endl;
else
    fout <<"Case #"<<num+1<<": "<<"IMPOSSIBLE" <<endl;


}
fin.close();
fout.close();
return 0;}
