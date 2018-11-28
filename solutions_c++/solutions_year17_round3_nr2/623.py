#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#include<iomanip>
#define PI 3.1415926535
using namespace std;

int main() {
  int T,Ac,Aj,ts,te;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>Ac>>Aj;
    vector<pair<int,pair<int,int> > > cam(Aj+Ac);
    for (int i=0;i<Ac;i++) {
      cin>>ts>>te;
      cam[i]=make_pair(ts,make_pair(te,0));
    }
    for (int i=0;i<Aj;i++) {
      cin>>ts>>te;
      cam[Ac+i]=make_pair(ts,make_pair(te,1));
    }
    sort(cam.begin(),cam.end());
    int starter = cam[0].second.second;
    int last = starter;
    int both=0,ctime=0,jtime=0,cpot=0,jpot=0;
    vector<int> cints;
    vector<int> jints;
    int changes = 0;
    for (int i=0;i<cam.size();i++) {
      int nexti = (i+1)%cam.size();
      if (cam[i].second.second) {
	jtime+=cam[i].second.first-cam[i].first;
	if (cam[nexti].second.second) {
	  jints.push_back((cam[nexti].first+1440-cam[i].second.first)%1440);
	  jpot+=(cam[nexti].first+1440-cam[i].second.first)%1440;
	} else {
	  changes++;
	  both+=(cam[nexti].first+1440-cam[i].second.first)%1440;
	}
      } else {
	ctime+=cam[i].second.first-cam[i].first;
	if (cam[nexti].second.second==0) {
	  cints.push_back((cam[nexti].first+1440-cam[i].second.first)%1440);
	  cpot+=(cam[nexti].first+1440-cam[i].second.first)%1440;
	} else {
	  changes++;
	  both+=(cam[nexti].first+1440-cam[i].second.first)%1440;
	}
      }
    }
    sort(cints.begin(),cints.end());
    reverse(cints.begin(),cints.end());
    sort(jints.begin(),jints.end());
    reverse(jints.begin(),jints.end());
    //    cout<<jtime<<' '<<jpot<<' '<<ctime<<' '<<cpot<<' '<<both<<endl;
    if (jtime+jpot+both >= 720 && ctime + cpot+both >= 720) {
      cout<<"Case #"<<t<<": "<<changes<<endl;
      continue;
    }
    int idx=0;
    while(jtime+jpot+both < 720) {
      jtime+=cints[idx];
      idx++;
      changes+=2;
    }
    idx=0;
    while(ctime+cpot+both < 720) {
      ctime+=jints[idx];
      idx++;
      changes+=2;
    }
    cout<<"Case #"<<t<<": "<<changes<<endl;
  }
}

