#include<iostream>
using namespace std;

bool check (int k){
while (k!=0){
if ((k%10)<((k/10)%10)) return false;
else k=k/10;}
return true;
}

int main(){
int t, n, i;
cin >> t;
for (int j=1; j<=t; j++){
cin >> n;
for (i=n; i>0; i--){
if (check (i)) {cout <<"Case #" << j << ": " << i << endl;
break;
}
}
}
}
