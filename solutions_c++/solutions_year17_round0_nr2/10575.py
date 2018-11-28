#include <iostream>
#include <string>
#include <fstream>

#define u unsigned long long
using namespace std;

u t , n;

bool is_tidy(u n){
u last_cif = 10;
while(n){
    if(n % 10 > last_cif)
    {
        return 0;
    }
    if(last_cif == 0)
    {
        return 0;
    }
    last_cif = n%10;
    n/=10;

}
return 1;
}

ifstream fin("in.in");
ofstream fout("out.in");

int main(){
fin>>t;
for(u i = 0 ; i < t; i++){
    fin>>n;
    if(is_tidy(n)){fout<<"Case #"<<i+1<<": "<<n<<'\n';}
    else{
        while(1){
            n--;
            if(is_tidy(n)){
                fout<<"Case #"<<i+1<<": "<<n<<'\n';
                break;
            }
        }
    }
}


return 0;
}

