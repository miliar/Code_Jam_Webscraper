#include<iostream>
#include<iomanip>
using namespace std;

int main(){

    int cases;
    long double destination;
    int number_of_horse;
    long double horse_initial_position,speed;
    cin>>cases;
    for(int i=0;i<cases;i++){
       cin>>destination>>number_of_horse;

       float maximum_time = 0;
       for(int j=0;j<number_of_horse;j++){
        cin>>horse_initial_position>>speed;

        if((destination-horse_initial_position)/speed  > maximum_time)
        {
           maximum_time= (destination-horse_initial_position)/speed ;
        }
       }
       std::cout << std::fixed;
       std::cout << std::setprecision(6);
       cout<<"Case #"<<i+1<<": "<<destination/maximum_time<<endl;
    }
}
