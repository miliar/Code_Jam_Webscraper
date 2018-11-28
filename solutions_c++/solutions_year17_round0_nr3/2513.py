#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

void maxminLsRs(long long int n, long long int k,long long int &ls,long long int &rs){
    long long int size_now = 1,size_prev=0,size_change=0;
    long long int now = n,count = 1,nowtemp,counttemp;
    long long int next1,next2,count1,count2;
    bool different_next = false;
    next1 = now; count1 = count;
    /*if(now%2 == 1){
        different_next = false;
        next1 = (now-1)/2;
        count1 = 2*count;
        size_change=2*count;
    }
    else{
        different_next = true;
        next1 = (now-1)/2;
        count1 = count;
        next2 = (now-1) - ((now-1)/2);
        count2 = count;
        size_change=2*count;
    }
    size_prev = size_now;
    size_now += size_change;*/

    while(size_now < k){
        if(different_next == false){
            now = next1;
            count = count1;
            if(now%2 == 1){
                different_next = false;
                next1 = (now-1)/2;
                count1 = 2*count;
                size_change=2*count;
            }
            else{
                different_next = true;
                next1 = (now-1)/2;
                count1 = count;
                next2 = (now-1) - ((now-1)/2);
                count2 = count;
                size_change=2*count;
            }
            size_prev = size_now;
            size_now += size_change;
        }
        else{
            if(next1 % 2 == 1){
                nowtemp = next2;
                counttemp = count2;
                now = next1;
                count = count1;
            }
            else{
                nowtemp = next1;
                counttemp = count1;
                now = next2;
                count = count2;
            }

            //different_next = false;
            next1 = (now-1)/2;
            count1 = 2*count;

            different_next = true;
            if(now > nowtemp){
                count1 += counttemp;
                next2 = ((nowtemp-1)/2);
                count2 = counttemp;
            }
            else{
                count1 += counttemp;
                next2 = (nowtemp-1) - ((nowtemp-1)/2);
                count2 = counttemp;
            }

            size_change=2*counttemp+2*count;
            size_prev = size_now;
            size_now += size_change;
        }
    }

    if(different_next == false){
        rs = (next1-1)/2;
        ls = next1-1 - ((next1-1)/2);
    }
    else{
        if(next1 >= next2){
            if(k <= size_prev + count1){
                rs = (next1-1)/2;
                ls = next1-1 - ((next1-1)/2);
            }
            else{
                rs = (next2-1)/2;
                ls = next2-1 - ((next2-1)/2);
            }
        }
        else{
            if(k <= size_prev + count2){
                rs = (next2-1)/2;
                ls = next2-1 - ((next2-1)/2);
            }
            else{
                rs = (next1-1)/2;
                ls = next1-1 - ((next1-1)/2);
            }
        }
    }
}

int main()
{
	int num_test_cases;
	long long int k,n,ls = 0,rs = 0;
	vector<long long int> v1;
	vector<long long int> v2;

	cin>>num_test_cases;

	for(int i=1; i <= num_test_cases; i++){
		cin>>n>>k;
		v1.push_back(n);
		v2.push_back(k);
	}

	for(int i=0; i < num_test_cases; i++){
		n = v1[i];
		k = v2[i];
		maxminLsRs(n,k,ls,rs);

        if(ls >= rs)
            cout << "Case #"<<i+1<<": "<<ls<<" "<<rs<<endl;
        else
            cout << "Case #"<<i+1<<": "<<rs<<" "<<ls<<endl;
	}

	return 0;
}
