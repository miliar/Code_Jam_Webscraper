#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

ifstream in("C-small.in");
ofstream out("out.out");

using namespace std;

long long pot2Magg(long long n){
    long long i=1;
    n/=2;
    while(n>=i)i*=2;
    return i;
}

int main()
{
    int caso,ncasi;
    in>>ncasi;
    long long nBagni,nPersone,min,max,tmp;
    for (caso=1;caso<=ncasi;caso++){
        in>>nBagni>>nPersone;
        long long nBagniLiberi=nBagni-nPersone;
        long long nBagniLiberiPerPersona=nBagniLiberi/pot2Magg(nPersone);
        min=nBagniLiberiPerPersona/2;
        max=nBagniLiberiPerPersona-min;
//        priority_queue<long long> bagni;
//        bagni.push(nBagni);
//        for (int i=0;i<nPersone;i++){
//            tmp=bagni.top(); bagni.pop();
//            while(tmp==0) {tmp=bagni.top(); bagni.pop();}
//            min=(tmp-1)/2; max=tmp/2;
//            bagni.push(max); bagni.push(min);
//        }

        out<<"Case #"<<caso<<": "<<max<<" "<<min<<endl;
    }
    return 0;
}
