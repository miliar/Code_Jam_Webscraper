#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    ofstream fout("out.txt");
int T;
cin>>T;
int N, R, O, Y, G, B, V;
for(int i=0;i<T;i++){
        fout<<"Case #"<<i+1<<": ";
    cin>>N>>R>>O>>Y>>G>>B>>V;


    if(R==G && N==R+G){
    for(int x=0;x<G;x++){
        fout<<"GR";
    }fout<<endl;
    continue;
    }
    if(Y==V && N==Y+V){
    for(int x=0;x<V;x++){
        fout<<"VY";
    }fout<<endl;
    continue;
    }
    if(B==O && N==B+O){
    for(int x=0;x<O;x++){
        fout<<"OB";
    }fout<<endl;
    continue;
    }


    if(R<=G && G!=0){fout<<"IMPOSSIBLE"<<endl;continue;}
    int Rn=R-G;
    if(Y<=V && V!=0){fout<<"IMPOSSIBLE"<<endl;continue;}
    int Yn=Y-V;
    if(B<=O && O!=0){fout<<"IMPOSSIBLE"<<endl;continue;}
    int Bn=B-O;
string sth;
    char last='-';
    //cout<<endl<<Rn+Yn+Bn<<endl;

int sum=Rn+Yn+Bn;


for(int x=0;x<3;x++){
if(Rn>Bn && Rn>Yn){for(int x=0;x<Rn;x++)sth+="R"; Rn=0;continue;}
if(Yn>Bn){for(int x=0;x<Yn;x++)sth+="Y"; Yn=0;continue;}
for(int x=0;x<Bn;x++)sth+="B"; Bn=0;
}


    string sub1=sth.substr(0,sum-sum/2);
    string sub2=sth.substr(sum-sum/2,sth.length());
  //  cout<<sth<<sub1<<sub2<<endl;
    sth="";
    for(int x=0;x<min(sub2.length(),sub1.length());x++){
        sth+=sub1[x];sth+=sub2[x];
    }if(sub2.length()>sub1.length())sth+=sub2[sub2.length()-1];
    if(sub2.length()<sub1.length())sth+=sub1[sub1.length()-1];
//fout<<sth<<endl;
    for(int x=0;x<sth.length()-1;x++){
        if(sth[x]==sth[x+1]){
            fout<<"IMPOSSIBLE"<<endl;goto out;
        }
    }
        if(sth[0]==sth[sth.length()-1]){
            fout<<"IMPOSSIBLE"<<endl;goto out;
        }

    //cout<<sth;
    if(true){
    size_t found = sth.find('R');
    if(found!=string::npos){
    for(int x=0;x<G;x++){sth.insert(found,"G");sth.insert(found,"R");}
    }
    found = sth.find('Y');
    if(found!=string::npos){
    for(int x=0;x<V;x++){sth.insert(found,"V");sth.insert(found,"Y");}
    }
    found = sth.find('B');
    if(found!=string::npos){
    for(int x=0;x<O;x++){sth.insert(found,"O");sth.insert(found,"B");}
    }
    }
    fout<<sth<<endl;

out:;
}
}
