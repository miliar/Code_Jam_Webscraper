#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream> 
#include <iomanip>


using namespace std;

string input;
vector<string> etapes;
string output;
ifstream is("test.in");
ofstream error("error.txt");
ofstream out("out.out");
int nbTest;

int dest;
int nbCav;
struct Cav {
	int speed;
	int pos;
	Cav(int pos_, int speed_) {
		pos = pos_;
		speed = speed_;
	}
};
void executeOneInput(){
	vector<Cav> cavs;
	is >> dest >> nbCav;
	for (int i = 0; i < nbCav; i++) {
		int speed;
		int pos;
		is >> pos >> speed;
		cavs.push_back(Cav(pos, speed));
	}
	double maxTimeArrival = 0;
	for (int i = 0; i < nbCav; i++) {
		Cav cav = cavs[i];
		double timeArrival = (float)(dest - cav.pos) / (float)cav.speed;
		if (timeArrival > maxTimeArrival)
			maxTimeArrival = timeArrival;
	}
	stringstream  ss;
	if(maxTimeArrival == 0)
		ss << fixed << setprecision(6) << dest / maxTimeArrival;
	else
		ss << fixed << setprecision(6) << dest / maxTimeArrival ;
	output = ss.str();



}
int main(int argc, char* argv[]){
	is >> nbTest;

	for(int i=0;i<nbTest;i++){
		executeOneInput();
		out << "Case #" << i + 1 << ": " << output << endl;

	}
}
