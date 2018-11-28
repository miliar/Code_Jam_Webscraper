#include<iostream>
#include<fstream>
using namespace std;
int main(){
ifstream in("A-large.in");
ofstream out("outA.txt");
string a;
int c,p,T;
bool imp = false;

in >> T;
for(int t=1;t <= T;t++){

c=0; imp=false;
in >> a;
in >> p;
//if(t==1 || t==3)cout << t << " "<<  a << "  " << p << endl;

for(int i=0;i<a.size();i++){
if(a[i]=='-')
if((a.size()-i) < p) {imp=true; break;}
else{
c++;
for(int j = i; j-i<p;j++){
    if(a.at(j)=='+')a.replace(j,1,"-");
    else a.replace(j,1,"+");
}
}
}
out << "Case #" << t << ": ";
if(!imp)out << c << endl;
else out << "IMPOSSIBLE" << endl;
}

out.close();
in.close();
return 0;
}
