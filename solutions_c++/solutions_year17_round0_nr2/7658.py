#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
long long parseArray(vector<int> inputArray)
{
    long long answer=0;
    for(int i=0;i<inputArray.size();i++){
        answer=answer*10+inputArray[i];
    }
    return answer;
}

void recurse(int min ,int max ,vector<long long> &x){

    while(min < max ){
        if(x[min] <= x[min+1])
            min++;
        else
            break;
    }
    if(min == max )
        return;
    else{
      x[min]--;
      for(int t=min+1;t <=max;t++)
        x[t]=9;
      recurse(0,min,x);
    }
}

void compute(vector<int> &x)
{
   int max = x.size()-1;
   int min=0;
   recurse(min,max,x);
}

long long findAnwser(long long x)
{
    vector<long long> inputArray;
    long long t=0;
    while(x!=0){
        t=x%10;
        x/=10;
        inputArray.push_back(t);
    }
    vector<long long> originalArray;

    for(int i=inputArray.size()-1;i >=0;i--){
        originalArray.push_back(inputArray[i]);
    }

    compute(originalArray);
    return (parseArray(originalArray));
}


int main(){
	int cases=0;
	long long input=0;
	cin>>cases;
	for(int i=0;i<cases;i++){
		cin>>input;
		cout<<"Case #"<<i+1<<":"<<" "<<compute(input)<<endl;
	}
    return 0;
}
