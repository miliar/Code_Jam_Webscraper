#include <iostream>
#include <queue>

using namespace std;


int main(){
    int cases;

    cin>>cases;
    int N, K; //N is the number of empty stalls & K is the number of persons in the bathroom
    int max, min;
    //queue<int> minMaxQ;

    for(int index=0;index<cases;index++){
        queue<int> minQ;
        queue<int> MaxQ;
        
        cin>>N>>K;
        if(N%2!=0 ){
            max= N/2;
            min= N/2;    
        }
        else{
            max= N/2;
            min= N/2 -1;  
        }
        MaxQ.push(max);
        minQ.push(min);
        int divisor;
        for(int person=1;person<K;person++){
            
            if(MaxQ.front()>minQ.front()){
                divisor=MaxQ.front();
                MaxQ.pop();
            }else{
                divisor=minQ.front();
                minQ.pop();
            }

            if(divisor%2!=0 ){
            max= divisor/2;
            min= divisor/2;    
            }
            else{
            max= divisor/2;
            if(divisor>0){
                min= divisor/2 -1;
            }
            }
            
            MaxQ.push(max);
            minQ.push(min);

        }

        cout<<"Case #"<<index+1<<": "<< max<<" "<<min<<endl;
        

    }
}