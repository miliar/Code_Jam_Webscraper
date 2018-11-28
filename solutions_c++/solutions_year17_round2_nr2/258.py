#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string repstr(string str, int i){
 string ret = "";
 while (i--) ret=ret+str;
 return ret;
}

int main() {
	int T;
	cin >> T;
	for (int it=1;it<=T;++it) {
		int n;
		int en[3];
		int tva[3];
		cin >> n >> en[0] >> tva[2] >> en[1] >> tva[0] >> en[2] >> tva[1];


		string stren, strtva;
		
		int tre[3];
		for (int i=0;i<3;++i) tre[i]=en[i]-tva[i];
		
	
		// SPECIAL CASE OF en[i]=tva[i] for some i, and the rest 0

		if (en[0]==tva[0] && en[1]+en[2]+tva[1]+tva[2]==0) {
			cout << "Case #" << it << ": " << repstr("RG", en[0]) << endl;
			continue;
		}
		if (en[1]==tva[1] && en[0]+en[2]+tva[0]+tva[2]==0) {
			cout << "Case #" << it << ": " << repstr("YV", en[1]) << endl;
			continue;
		}
		if (en[2]==tva[2] && en[1]+en[0]+tva[1]+tva[0]==0) {
			cout << "Case #" << it << ": " << repstr("BO", en[2]) << endl;
			continue;
		}
		
		// Create string with tre[0] R:s tre[1] Y:s and tre[2] B:s with no repeating characters.

		if ( tre[0]<0 ||tre[1] < 0 || tre[2] < 0 || (tre[0]==0 && tva[0]>0) || (tre[1]==0 && tva[1]>0) || (tre[2]==0 && tva[2]>0) ) {
			cout << "Case #" << it << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		int startcol, maxprev=-1;
		for (int i=0;i<3;++i) if (tre[i]>maxprev) {
			maxprev=tre[i];
			startcol=i;
		}

		string dic="RYB";
		int langd = tre[0]+tre[1]+tre[2];
		bool fuckup=false;
		for (int i=0;i<langd;++i) {

			int col, maxprev2=-1;
			for (int i=0;i<3;++i) {
				if (stren.length()==0 || stren[stren.length()-1] != dic[i]) if (tre[i]>maxprev2 || (tre[i] == maxprev2 && i==startcol )) {
					maxprev2=tre[i];
					col=i;
				}
			}
			stren = stren+dic[col];
			if (tre[col]<=0) fuckup=true;
			--tre[col];
		}
		if (stren[0]==stren[langd-1] || fuckup) {
			cout << "Case #" << it << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		int i=0;
		while (strtva.length()<n) {
			if ( stren[i]=='R' ) {
				if (tva[0]>0) {
					--tva[0];
					strtva=strtva+"RG";
				} else {
					strtva=strtva+"R";
					++i;
				}
			}
			if ( stren[i]=='Y' ) {
				if (tva[1]>0) {
					--tva[1];
					strtva=strtva+"YV";
				} else {
					strtva=strtva+"Y";
					++i;
				}
			}
			if ( stren[i]=='B' ) {
				if (tva[2]>0) {
					--tva[2];
					strtva=strtva+"BO";
				} else {
					strtva=strtva+"B";
					++i;
				}
			}


		}

		cout << "Case #" << it << ": " << strtva << endl;
/*		cout << n << endl;
		cout << en[0] << " " << en[1] << " " << en[2] << endl;
		int entest[3];
		entest[0]=entest[1]=entest[2]=0;
		for (int i=0;i<n;++i) for (int j=0;j<3;++j) if (dic[j]==strtva[i]) entest[j]++;
		cout << entest[0] << " " << entest[1] << " " << entest[2] << endl;
*/


	}
}