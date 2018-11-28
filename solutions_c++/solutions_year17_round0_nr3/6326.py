#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

ifstream infile("C-small-2-attempt0.in");
ofstream outfile("csmall_sol2.in");

int loga(int k){
    int i=0,p;
    while(pow(2,i)<=k){
        i++;
        }
    return i-1;
}
int main(){
int i=1;
int seat,memb;
int times;
infile>>times;
while(times--)
    {infile>>seat;
    infile>>memb;
    int layer=loga(memb);
    int fill_memb=pow(2,layer)-1;
    int spaces=fill_memb+1;
    int bef_memb=memb-fill_memb-1;
    int emp_seat=seat-fill_memb;
    int seat_size=(emp_seat)/spaces;
    int big_seat=emp_seat-(seat_size) *(spaces);
    int sizee;
    if(bef_memb>=big_seat)
        sizee=seat_size;
    else
        sizee=seat_size+1;
//cout<<sizee<<endl;
    sizee--;
    outfile<<"Case #"<<i<<": "<<sizee-sizee/2<<" "<<sizee/2<<endl;
    i++;
    }



}
