#include<iostream>
#include<fstream>
using namespace std;

int main(){
ofstream out("outC.txt");
ifstream in("C-small-2-attempt0.in");
int T;
long long n;
long long k;
in >> T;
for(int t= 1; t<=T;t++){
in >> n >> k;
long long r=n/2,l=(n-1)/2,nr=1,nl=1,level=2,total=2;

while(total/2+level < k){
level *= 2;
total += level;
if(r==l){nl=nr=level/2;}
else if(r%2==0){nr=nr; nl=level-nr;}
else{nl=nl; nr=level-nl;}
r/=2;l=(l-1)/2;

}
//cout << level << " " << total << " " << r << " " << l << " " <<nr << " "<<nl<<endl;
out << "Case #" << t <<": ";
if(k==1) out << n/2 <<" " << (n-1)/2 << endl;
else if(nr>=k-total/2)out << r/2 << " " << (r-1)/2 << endl;
else out << l/2 << " " << (l-1)/2 << endl;
}
in.close();
out.close();
return 0;
}
