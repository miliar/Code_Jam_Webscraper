#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
bool Tidy(string num,int size){
stringstream det;
det.str("");
 int n1;
 int n2;
 string p;

 if (size==1)
    return true;
for (int i=0;i<size-1;i++){
if (num[0]!='0'|| i!=0){
    det << num.substr(i,2);
      p=det.str();
     n1=p[0]-'0';
     n2=p[1]-'0';

    det.str("");


    if (n2<n1)
    {
        return false;

    }
}

}
return true;
}
string conv(string num,int size){
    string p=num;

int count=0;

   if (Tidy(p,size)==true)
    {
        return p;
    }
 while(count==0){

    for (int i=size-1;i>0;i--)
    {
        if(p[i]<p[i-1])
        {for (int j=i;j<size;j++)

            p[j]='9';
            p[i-1]=p[i-1]-1;

            break;    }

    }
     if(p[0]=='0')
     {
         for (int i=1;i<size;i++)
            p[i]='9';
            return p;
     }

     if (Tidy(p,size)==true)
    {
        return p;


 }



}

}





int main(){
 long long N   ;
 int T ;
  stringstream cp;
  string temp;
 ifstream fin;
 ofstream fout;

cp.str("");
fin.open("B-large.in.txt");
fout.open("A2.txt",ios::app);
fin >>T;

for (int count=0;count<T;count++){

fin >> N;

   cp <<N;
temp=conv(cp.str(),cp.str().length());
if (temp[0]=='0')

fout << "Case #"<<count+1<< ": "<< temp.substr(1,temp.length()-1) <<endl;
else

fout << "Case #"<<count+1<< ": "<< temp <<endl;

cp.str("");

}



fin.close();
fout.close();




























/*char S[1003];
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
fout.close();*/
return 0;}
