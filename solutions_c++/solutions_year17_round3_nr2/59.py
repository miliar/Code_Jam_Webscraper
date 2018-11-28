#include<bits/stdc++.h>
using namespace std;

struct task{
	bool Jam;
	long start;
	long end;

	bool operator<( const task& right ) const {
		return start < right.start;
	}

};

void solve(){
	long long AC, AJ;
	cin >> AC >> AJ;
	vector<struct task> tasks;

	long long twork = 0;
	long long cwork = 0;

	for(int i = 0; i < AC; i++){
		struct task t;
		t.Jam = true;
		cin >> t.start >> t.end;
		tasks.push_back(t);
		twork += t.end - t.start;
	}

	for(int i = 0; i < AJ; i++){
		struct task t;
		t.Jam = false;
		cin >> t.start >> t.end;
		tasks.push_back(t);
		cwork += t.end - t.start;
	}
	sort(tasks.begin(), tasks.end());

	long long ans = 0;
	vector<long long> jtime;
	vector<long long> ctime;

	if(tasks.size() == 1){
		cout << 2 << endl;
		return;
	}

	if(tasks[0].Jam != tasks[tasks.size() - 1].Jam){
		ans++;
	}

	for(int i = 0; i < tasks.size() - 1; i++){
		if(tasks[i].Jam != tasks[i+1].Jam){
			ans++;
		}
	}

	if(tasks[0].Jam == tasks[tasks.size() - 1].Jam){
		long long time = tasks[0].start + 1440 - tasks[tasks.size()-1].end;
		if(tasks[0].Jam == true){
			jtime.push_back(time);
		}else{
			ctime.push_back(time);
		}
	}

	for(int i = 0; i < tasks.size() - 1; i++){
		if(tasks[i].Jam == tasks[i+1].Jam){
			long long time = tasks[i+1].start -  tasks[i].end;
			if(tasks[i].Jam == true){
				jtime.push_back(time);
			}else{
				ctime.push_back(time);
			}
		}
	}

	sort(jtime.begin(), jtime.end());

	sort(ctime.begin(), ctime.end());

	/*
	cout << "jtime " << endl;
	for(int i = 0; i < jtime.size(); i++){
		cout << jtime[i] << endl;
	}
	cout << "ctime " << endl;
	for(int i = 0; i < ctime.size(); i++){
		cout << ctime[i] << endl;
	}
	cout << "twork = " << twork << endl;
	*/


	while(1){
		if(jtime.size() == 0){
			break;
		}
		if(twork + jtime[0] > 720){
			break;
		}
		twork += jtime[0];
		jtime.erase(jtime.begin());
	}

	while(1){
		if(ctime.size() == 0){
			break;
		}
		if(cwork + ctime[0] > 720){
			break;
		}
		cwork += ctime[0];
		ctime.erase(ctime.begin());
	}
	cout << ans + 2*ctime.size() + 2*jtime.size() << endl;

}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

