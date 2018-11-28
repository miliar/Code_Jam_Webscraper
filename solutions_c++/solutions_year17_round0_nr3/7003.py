#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int xx = 1; xx <= t; ++xx)
	{
		long n,k;
		cin>>n>>k;
		/*
		cout<<endl;
        cout<<n<<" "<<k<<" "<<endl;
        //*/

		multiset <long> occupiedIndex;
		vector <bool>  occupied(n+2,false);
		occupied[0] =true;
		occupied[n+1] = true;

		occupiedIndex.insert(0);
		occupiedIndex.insert(n+1);

        // setting first person
		long m = n/2;

		if(n%2!=0) m++;
		if(n==1) m=1;
		occupied[m]=true;
		occupiedIndex.insert(m);
        //..

        /*
		for(int i=0;i<n+2;i++){
        cout<<occupied[i]<<" ";
        }
        cout<<endl;
        */

    long mid = m;
     //cout<<"occupied:"<<mid<<endl;
    for(int person = 1 ; person < k ;person++){

        auto it = occupiedIndex.begin();
        it++;
        long maxx = 0;
        mid = 0;

		while(it != occupiedIndex.end()){

            it--;
            int a = *(it);
            it++;
            int b = *(it);

            if(maxx < b-a-1){

                    maxx = b-a-1;
                    mid = (a+b)/2;
                    //if(maxx%2==0 && maxx!=2) mid--;
                    //cout<<"changed:"<<a<<" "<<b<<" "<<mid<<endl;
            }
            it++;
		}
        //cout<<"occupied:"<<mid<<endl;
		occupiedIndex.insert(mid);
		occupied[mid]=true;
    }

    /*
    for(int i=0;i<n+2;i++){
        cout<<occupied[i]<<" ";
    }
    cout<<endl;
    cout<<"last mid:"<<mid<<endl;
    //*/


    int ls=0,rs=0;

    int i = mid-1;
    while(i>=0 && occupied[i] != true ){
        ls++;
        i--;
    }

    int j = mid+1;
    while( j<= n+1 && occupied[j] != true ){
        rs++;
        j++;
    }

    if(ls>rs)
    cout<<"Case #"<<xx<<": "<<ls<<" "<<rs<<endl;
    else
    cout<<"Case #"<<xx<<": "<<rs<<" "<<ls<<endl;


	}



	return 0;
}
