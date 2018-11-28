#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	vector< pair<int,int> > a;
	char values[6] = {'R', 'O', 'Y', 'G', 'B', 'V' };
	std::list< char > ans;		
	bool debug = false;
	for(int ti =1;ti<=t;ti++)
	{
		a.clear();
		ans.clear();
		int n;
		cin>>n;
		int x;
		for(int i =0;i<6;i++)
		{
			cin>>x;
			a.push_back(make_pair(x,i));
		}
		int i;
		char cur;
		for( i=0;i<6;i++ )
		{
			if(a[i].first != 0 )
			{
				for(int j=0;j< a[i].first;j++)
					ans.push_back( values[a[i].second ] );

				cur = values[a[i].second];				
				break;
			}				
		}	
		if( debug )
		{
			cout<<endl<<i<<"first loop"<<endl;
			for( auto it= ans.begin( );it!=ans.end();it++ )
			{
				cout<<*it;
			}
		}
		for( i = i+1;i<6;i++)
		{
			if( a[i].first != 0 )
			{
				if( debug )
				{
					cout<< i << " "<< "before all"<<a[i].first<<endl;

				}
				while( a[i].first )
				{
					auto it= ans.begin( );
					cur = *(ans.rbegin());
					for( it = it;it!=ans.end();it++)
					{
						if( cur == *it )
						{
							ans.insert( it, values[a[i].second]);
							a[i].first --;
							if( a[i].first == 0 )
							{
								break;
							}
						}
						cur = *it;
					}
					break;
				}
				if( debug )
				{
					cout<<endl<<i<<" after same"<<a[i].first<<endl;
					for( auto it= ans.begin( );it!=ans.end();it++ )
					{
						cout<<*it;
					}
				}

				while( a[i].first )
				{
					auto it= ans.begin( );
					char prev = *(ans.rbegin() );
					cur = *it;
					for( it = it;it!=ans.end();it++)
					{
						cur = *it;
						//bool setprev = true;
						if( (cur != values[ a[i].second ]) && (prev != values[ a[i].second ]) )
						{
							ans.insert( it, values[a[i].second]);
							//prev = values[a[i].second];
							//setprev = false;
							a[i].first --;
							if( a[i].first == 0 )
							{
								break;
							}
						}
						prev = *it;
					}
					break;
				}
				if( debug )
				{
					cout<<endl<<i<<" after non-equal"<<a[i].first<<endl;
					for( auto it= ans.begin( );it!=ans.end();it++ )
					{
						cout<<*it;
					}
				}
				
				for( int j  = 0; j < a[i].first; j++ )
				{
					ans.push_back( values[a[i].second]);		
				}
				a[i].first = 0;
			}
			if( debug )
			{
				cout<<endl<<i<< " last"<<a[i].first<<endl;
				for( auto it= ans.begin( );it!=ans.end();it++ )
				{
					cout<<*it;
				}
				cout<<"size"<<ans.size()<<endl;
			}

		}
		double isPossible = true;
		char prev = *(ans.rbegin());
		for( auto it = ans.begin(); it!= ans.end(); it++)
		{
			if( prev == *it )
			{
				isPossible = false;
				break;
			}
			prev = *it;
		}
		cout<<"Case #"<<ti<<": ";
		if( !isPossible )
		{
			cout<<"IMPOSSIBLE";
		}
		else{
				for( auto it= ans.begin( );it!=ans.end();it++ )
				{
					cout<<*it;
				}			
		}
		cout<<endl;
	}
	return 0;
}