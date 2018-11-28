#include <algorithm>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		int AC, AJ;

		cin>>AC>>AJ;

		vector <pair<pair <int, int>, int> > tasks,J;

		for(int i=0;i<AC;++i) {
			int tmpc,tmpd;
			cin>>tmpc>>tmpd;
			tasks.push_back(make_pair(make_pair(tmpc, tmpd),0));
		}
		for(int i=0;i<AJ;++i) {
			int tmpc,tmpd;
			cin>>tmpc>>tmpd;
			tasks.push_back(make_pair(make_pair(tmpc, tmpd),1));
		}

		sort(tasks.begin(), tasks.end());

		tasks.push_back(make_pair(make_pair(tasks[0].first.first + 1440, tasks[0].first.second + 1440), tasks[0].second));

		int currentwork[2];
		currentwork[0]=0;
		currentwork[1]=0;

		vector <vector <int> > stock;

		stock.push_back(vector <int>());
		stock.push_back(vector <int>());

		int curusr=-1;
		int curprev=-1;

		int flips=0;

		for (int i=0; i<tasks.size(); ++i){
			if (curusr == tasks[i].second){
				currentwork[curusr] += tasks[i].first.second - tasks[i-1].first.second;
				stock[curusr].push_back(tasks[i].first.first - tasks[i-1].first.second);
			} else {
				curusr = tasks[i].second;
				if (i>0){
					flips++;
					currentwork[curusr] += tasks[i].first.second - tasks[i].first.first;
				}
			}
		}

		for (int usr=0; usr<2; ++usr) {
			sort(stock[usr].begin(), stock[usr].end());
			while(currentwork[usr] > 720) {
				flips += 2;
				currentwork[usr] -= stock[usr][stock[usr].size()-1];
				stock[usr].pop_back();

			}
		}


		cout << flips << endl;


	}
}

