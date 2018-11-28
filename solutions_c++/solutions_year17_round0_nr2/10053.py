#include<iostream>

using namespace std;

int sies(int num, int cop){
    int d1,d2,numco;
    cop=num;
     d1=num%10;
    while(num!=0)
    {
            num/=10;
            d2=num%10;
            //cout<<"D1 "<<d1;
          //  cout<<"  D2 "<<d2;

            if(d1<d2)
            {
                //cout<<"D1 ES MENOR A D2 "<<endl;
                cop--;
              // cout<<"NUM NUEVO FUNCION  "<<cop<<endl;
                return sies(cop,cop);
            }
             d1=d2;
    }
    if(num==0)
    return cop;
}


int main(){
    int cases=0;
    int num;
    cin>>cases;
    for(int i=0; i<cases;i++)
    {
        cin>>num;
        cout<<"Case #"<<i+1<<": ";
        cout<<sies(num,num);
        cout<<endl;
    }

return 0;
}
