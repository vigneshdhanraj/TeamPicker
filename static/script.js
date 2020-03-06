$( document ).ready(function() {
	var n, k, str = '';
	for(k = 0; k <=1; k++) {
		for(n = 0; n <= 10; n++) {
			str += '<div>' +
			        '<label for="Name">Name:</label>' +
        			'<input type="text" id="Name_' + k + '_' + n + '">' +
		        	'<label for="Role">Role:</label>' +
	        		'<select id="Role_' + k + '_' + n + '">' +
 		 			'<option value="BAT">BAT</option>' +
			        	'<option value="BOWL">BOWL</option>' +
				        '<option value="ALL">ALL</option>' +
			        	'<option value="WK">WK</option>' +
		        	'</select>' +
		        	'<label for="Credit">Credit:</label>' +
			        '<input type="text" id="Credit_' + k + '_' + n + '">' +
			'</div>';
		}
		str += '<p></p>';
	}
	$('body').prepend(str);



	$('body').delegate('#submitBtn', 'click', function(e) {
		var n, k, obj = {"Team": [{"Team1": []}, {"Team2": []}]}, tmp;
	        for(k = 0; k <=1; k++) {
        	        for(n = 0; n <= 10; n++) {
				tmp = {};
				tmp['Name'] = $('#Name_' + k + '_' + n).val();
				tmp['Role'] = $('#Role_' + k + '_' + n).val();
				tmp['Credit'] = $('#Credit_' + k + '_' + n).val();
				obj['Team'][k]['Team' + (k + 1)].push(tmp);
			}
		}
		$.ajax({
			method: "POST",
			url: "/Getplaylist",
			contentType: "application/json, charset=UTF-8",
			data: JSON.stringify(obj)
		}).done(function(msg) {
			alert("Success");
		});
	});
});
