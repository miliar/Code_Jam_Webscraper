#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int main()
{
	long long int t;
	long long int ans_max, ans_min, n, k;
	long long int digits[65];
	cin>>t;
	map<long long int, long long int > count_map;
	map<long long int, long long int > count_map_alt;
	vector< pair<long long int, long long int> > avail_arr;
	for(long long int ti =1;ti<=t;ti++)
	{
		avail_arr.clear();
		count_map_alt.clear();
		count_map.clear();
		cin>>n>>k;

		long long int level_k = 0;
		long long int alt_k = k;
		while(alt_k>0)
		{
			alt_k/=2;
			level_k++;
		}
		long long int i = 1;
		count_map[n] = 1;
		while( i< level_k)
		{
			for( auto it = count_map.begin(); it != count_map.end(); it++ )
			{
				long long int min_avail = (it->first-1)/2;
				long long int max_avail = (it->first)/2;
				if( !count_map_alt.count( min_avail ) )
					count_map_alt[min_avail] = it->second;
				else
					count_map_alt[min_avail] += it->second;

				if( !count_map_alt.count( max_avail ) )
					count_map_alt[max_avail] = it->second;
				else
					count_map_alt[max_avail] += it->second;
			}
			count_map.clear();
			for( auto it = count_map_alt.begin(); it != count_map_alt.end(); it++ )
				count_map[it->first] = it->second;
			count_map_alt.clear();
			i++;
		}
		for( auto it = count_map.begin(); it != count_map.end(); it++ )
		{
			avail_arr.push_back( make_pair( it->first, it->second ) );
		}
		sort( avail_arr.begin(), avail_arr.end());
				
		long long int avail = 0;
		long long int remaining = k - (1<<level_k-1)+1;
		//cout<<remaining<<endl;
		long long int cdf = 0;
		for( long long int j = avail_arr.size() -1; j>=0; j-- )
		{
			if( cdf >= remaining )
				break;
			avail = avail_arr[j].first;
			cdf = avail_arr[j].second + cdf;
		}		
		/*
		for( long long int j= avail_arr.size() -1; j>=0; j-- )
		{
			cout<<avail_arr[j].first<< " "<<avail_arr[j].second<<endl;
		}
		cout<<"avail "<<avail<<endl;
		*/
		/*
		long long int avail = n;

		if(k>1)
		{
			long long int min_avail = (avail-1)/2;
			long long int max_avail = avail/2;
			long long int count_max_avail;
			count_max_avail = (max_avail==min_avail)?2:1;
			long long int count_min_avail = 2-count_max_avail;
			long long int i = 1;
			while( i < level_k - 1 ) 
			{

				long long int temp_max_avail = max_avail/2;
				long long int count_max_avail_temp = count_max_avail;
				if( ( max_avail-1 )/2 == temp_max_avail )
					count_max_avail_temp += count_max_avail;
				if( ( min_avail-1 )/2 == temp_max_avail )
					count_max_avail_temp += count_min_avail;
				min_avail = (max_avail-1)/2;
				max_avail = temp_max_avail;
				if(min_avail==max_avail)
					count_max_avail_temp += count_min_avail;
				long long int count_min_avail_temp = 2*(count_max_avail+count_min_avail)-count_max_avail_temp;
				count_max_avail = count_max_avail_temp;
				count_min_avail = count_min_avail_temp;
				i++;				
			}
			if( count_max_avail >  )
				avail = max_avail;
			else
				avail = min_avail;
			cout<<avail<<" "<< max_avail<<" "<<min_avail<<" "<<count_max_avail<< " "<<count_min_avail<<" "<<level_k<<" "<<n<<" "<<k<<endl;			
			
		}
		*/
		long long int ans_max = avail/2;
		long long int ans_min =  (avail-1)/2;

		cout<<"Case #"<<ti<<": "<<ans_max<< " "<<ans_min<<endl;
	}
	return 0;
}