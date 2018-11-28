#include <bits/stdc++.h>
using namespace std;


string int2str(int a)
{
	stringstream ss;
	ss << a;
	return ss.str();
}


int n,k;

struct tuple_pq
{
    int a;
    int b;
    int diff;
    bool operator<(const tuple_pq& rhs) const
    {
        return diff < rhs.diff;
    }
};

int main()
{
	int test_case;
	cin>>test_case;
	for(int abc=0;abc<test_case;abc++)
	{
		// cout<<"Case #"<<(abc+1)<<": "<<i<<endl;
		cin>>n>>k;
		priority_queue<tuple_pq> my_pq;
		tuple_pq newtp;
		newtp.a=1;
		newtp.b=n+2;
		newtp.diff=(newtp.b-newtp.a);
		my_pq.push(newtp);
		// cout<<"start"<<endl;
		for(int t=0;t<k-1;t++)
		{
			tuple_pq top_pq=my_pq.top();
			my_pq.pop();
			int chosen=(top_pq.a+top_pq.b)/2;
			tuple_pq left_tp;
			left_tp.a=top_pq.a;
			left_tp.b=chosen;
			left_tp.diff=(left_tp.b-left_tp.a);
			my_pq.push(left_tp);
			tuple_pq right_tp;
			right_tp.a=chosen;
			right_tp.b=top_pq.b;
			right_tp.diff=(right_tp.b-right_tp.a);
			my_pq.push(right_tp);
			// cout<<"chose :"<<chosen<<endl;
		}
		tuple_pq top_pq=my_pq.top();
		int chosen=(top_pq.a+top_pq.b)/2;
		int left_gap=(chosen-top_pq.a-1);
		int right_gap=(top_pq.b-chosen-1);
		// cout<<"chose :"<<chosen<<endl;
		cout<<"Case #"<<(abc+1)<<": "<<max(left_gap,right_gap)<<" "<<min(left_gap,right_gap)<<endl;
	}
	return 0;
}

