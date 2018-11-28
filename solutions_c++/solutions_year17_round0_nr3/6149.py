#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

#define STRSIZE 256

bool myfunction (int i,int j) { return (i>j); }

int main (int argc, char* argv[]) {

	string infile;
	string outfile;
	
	if (argc != 3) {
		printf("Usage: tidy-numbers [infile] [outfile]\n");
		exit(1);
	} else {
		infile = string(argv[1]);
		outfile = string(argv[2]);
	}
	
	int cases;
	
	// Contains (n,k) pairs
	vector<pair<int,int> > parameters;
	
	// Contains (max(L_s,R_s),min(L_s,R_s)) pairs
	vector<pair<int,int> > output;
	
	char linebuf_cstr[STRSIZE];
	FILE *infile_ptr = fopen(infile.c_str(), "r");
	int line_num = 1;
	while (fgets(linebuf_cstr, STRSIZE-1, infile_ptr) != NULL) {
	
		string linebuf = string(linebuf_cstr);
		linebuf.erase(linebuf.find_last_not_of(" \n\r\t")+1);
		// int num = atoi(linebuf.c_str());
		
		if (line_num == 1) {
			cases = atoi(linebuf.c_str());
		} else {
			unsigned int pos = linebuf.find_first_of(" ");
			string n = linebuf.substr(0,pos);
			string k = linebuf.substr(pos+1);
			pair<int,int> temp (atoi(n.c_str()), atoi(k.c_str()));
			parameters.push_back(temp);
		}
		line_num++;
	}
	if (!(feof(infile_ptr)) && ferror(infile_ptr)) { // This is an error
		char preamble[STRSIZE];
		sprintf(preamble, "There was an error reading from %s", infile.c_str());
		perror(preamble);
		return 1;
	}
	fclose(infile_ptr);
	
	for (unsigned int i = 0; i < parameters.size(); i++) {
		int n = parameters[i].first;
		int k = parameters[i].second;
		
		int cur_max;
		int cur_min;
		
		// Initialize first row, and index pointer
		vector<int> cur_row (1,n);
		int cur_index = 0;
		vector<int> next_row (2,0);
		int next_index = 0;
		
		for (int j = 0; j < k; j++) {
			int split = cur_row[cur_index];
			
// 			if (split == 0) {
// 				break;
// 			}
			
			// Outcome depends on even/odd
			if (split % 2) { // Odd
				int new_dist = (split-1)/2;
				next_row[next_index] = new_dist;
				cur_max = new_dist;
				next_index++;
				next_row[next_index] = new_dist;
				cur_min = new_dist;
				next_index++;
			} else { // Even
				int new_dist1 = split/2;
				int new_dist2 = (split-2)/2;
				next_row[next_index] = new_dist1;
				cur_max = new_dist1;
				next_index++;
				next_row[next_index] = new_dist2;
				cur_min = new_dist2;
				next_index++;
			}
			
			// Update indices
			cur_index++;
			if (cur_index == cur_row.size()) { // Time for a new row
				cur_row = next_row;
				sort(cur_row.begin(), cur_row.end(), myfunction);
				cur_index = 0;
				vector<int> temp (2*cur_row.size(),0);
				next_row = temp;
				next_index = 0;
			}
		}
		
		pair<int,int> tmp (cur_max,cur_min);
		output.push_back(tmp);
	}
	
	// Print output
	FILE *outfile_ptr = fopen(outfile.c_str(), "w");
	for (unsigned int i = 0; i < output.size(); i++) {
		fprintf(outfile_ptr, "Case #%d: %d %d\n", i+1, output[i].first, output[i].second);
	}
	fclose(outfile_ptr);
	return 0;
}
