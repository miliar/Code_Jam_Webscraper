#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream> 


using namespace std;

string input;
vector<string> etapes;
string output;
ifstream is("test.in");
ofstream error("error.txt");
ofstream out("out.out");
int nbTest;


void executeOneInput(){
	int nbColor;
	int color[6];
	is >> nbColor >> color[0] >> color[1] >> color[2] >> color[3] >> color[4] >> color[5];
	int iRed = color[0] + color[1] + color[5];
	int iYellow = color[1] + color[2] + color[3];
	int iBlue = color[3] + color[4] + color[5];
	char colorsChar[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
	if (iRed > iYellow + iBlue || iBlue > iYellow + iRed || iYellow > iRed + iBlue)
		output = "IMPOSSIBLE";
	else {
		string suite;
		int nextElement = 0;
		int nbElement = color[0];
		for (int i = 1; i < 6; i++) {
			if (color[i] > nbElement) {
				nextElement = i;
				nbElement = color[i];
			}
		}
		suite += colorsChar[nextElement];
		color[nextElement]--;
		int previousColor = nextElement;
		for (int k = 0; k < nbColor-1; k++) {
			stringstream  ss;
			ss << color[0] << " " << color[1] << " " << color[2] << " " << color[3] << " " << color[4] << " " << color[5];
			etapes.push_back(ss.str());
			nextElement = (previousColor+2)%6;
			nbElement = color[nextElement];
			for (int i = 0; i < 6; i++) {
				if (i != previousColor && i != (previousColor + 1) % 6 && i != (previousColor - 1) % 6){
					if (color[i] > nbElement) {
						nextElement = i;
						nbElement = color[i];
					}
					else if (color[i] == nbElement && i%2 == 1) {
						nextElement = i;
						nbElement = color[i];

					}
				}
			}
			suite += colorsChar[nextElement];
			color[nextElement]--;
			previousColor = nextElement;


		}
		output = suite;
	}

}
int main(int argc, char* argv[]){
	is >> nbTest;

	for(int i=0;i<nbTest;i++){
		executeOneInput();
		out << "Case #" << i + 1 << ": " << output << endl;

	}
}
